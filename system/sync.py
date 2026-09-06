#!/usr/bin/env python3
"""
sync.py -- the "change it once" tool for this repo.

WHY IT EXISTS (user, 2026-09-05): "whenever we make a small change, there is, like, I don't know how many
documents that list the change and need to be fixed. All of this is just too much. We need a way for all of
this to be easier and more fluent and more automatic."

Measured before building this: the agency palette was restated in 26 files, demo-house status in 20,
pricing in 9. Every one was a chance to go stale, and whichever copy got missed became the lie that misled
the next freshly-spawned agent.

TWO JOBS
  1. FACTS  -- regenerate every AUTO block from system/facts.json, the one machine-readable home for facts
               that many documents repeat. You edit facts.json; the documents update themselves.
  2. LINKS  -- verify that repo paths named in live docs actually exist, so a moved file cannot silently
               leave a dozen dead references behind (this is how the retired the demo brand hero and the
               brand/[client]-logo path both rotted).

USAGE
  python system/sync.py            # check only, changes nothing, non-zero exit if drift or dead links
  python system/sync.py --write    # rewrite AUTO blocks to match facts.json
  python system/sync.py --links    # only the link check
  python system/sync.py --facts    # only the facts check

AUTO BLOCKS
  A managed region in any markdown file looks like:
      *(generated block: add the fact to `system/facts.json`, mark the spot with an AUTO block, then run `python system/sync.py --write`)*
  Text outside the markers is yours and is never touched. To put a fact somewhere new, paste an empty
  pair of markers with a known block name and run --write.

APPEND-ONLY FILES ARE NEVER TOUCHED. changelog.md, progress.md, qc-log.md, creative-decisions-log.md,
job tickets and anything under _archive/ or _drafts/ are historical records of what was true at the time.
Rewriting them would destroy the audit trail, which is the opposite of the point.
"""
import io, os, re, sys, json

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FACTS = os.path.join(ROOT, "system", "facts.json")

FROZEN = ("changelog.md", "progress.md", "qc-log.md", "creative-decisions-log.md",
          "next-session-prompt.md")
# NOTE: forward slashes only. rel paths are normalised to "/" before these are tested, and an
# os.path.join here silently produced "system\\jobs" on Windows, which matched nothing and made the
# first run of this tool spew 74 findings from frozen job tickets. Noise is what makes a checker
# get ignored, so this matters more than it looks.
# Append-only history, per LAW 4 of system/file-system-law.md: these record what was true at the
# time and are never rewritten, so a stale path inside them is correct, not rot.
# "_archive/" and "_drafts/" are gone (LAW 4 abolished them); "_alts/" replaced them.
FROZEN_DIRS = ("_alts/", "system/jobs/", "/prompts/", "/qc-notes/",
               ".git/", ".claude/skills/", ".hermes/skills/", "OpenMontage/")


def load():
    with io.open(FACTS, encoding="utf-8") as fh:
        return json.load(fh)


# ---------------------------------------------------------------- block builders

def block_palette(d):
    m = d["[client]"]
    out = ["| Role | Name | Hex |", "|---|---|---|"]
    for c in m["palette"]:
        out.append("| %s | %s | `%s` |" % (c["role"], c["name"], c["hex"]))
    out.append("")
    out.append("**RETIRED, never use:** " + " / ".join("`%s`" % h for h in m["palette_retired"]) + ".")
    out.append("")
    out.append("*Generated from `system/facts.json` by `system/sync.py`. Do not hand-edit this block; "
               "change the value there and run `python system/sync.py --write`.*")
    return "\n".join(out)


def block_demo_roster(d):
    m = d["[client]"]
    out = ["| House | Category | Spec file (source of truth) | Identity | Locked hero | Status |",
           "|---|---|---|---|---|---|"]
    for h in m["demo_houses"]:
        hero = ("`%s`" % h["hero"]) if h["hero"] else "not generated"
        out.append("| **%s** | %s | `%s` | %s | %s | %s |"
                   % (h["name"], h["category"], h["spec"], h["identity"], hero, h["status"]))
    out.append("")
    out.append("*Generated from `system/facts.json` by `system/sync.py`. Do not hand-edit this block.*")
    return "\n".join(out)


def block_dbmedia_summary(d):
    m = d["[client]"]
    pal = ", ".join("%s `%s`" % (c["name"], c["hex"]) for c in m["palette"])
    lines = [
        "**%s** (formerly %s, renamed %s; future home %s). Type: %s" %
        (m["name"], m["former_name"], m["renamed"], m["future_home"], m["type"]),
        "",
        "- **Gate:** %s" % m["gate"],
        "- **Palette:** %s" % pal,
        "- **Logo kit:** `%s` · **Brand profile (source of truth):** `%s`" % (m["logo_dir"], m["brand_profile"]),
        "- **Pricing:** " + " / ".join("%s $%d" % (t["tier"], t["usd_month"]) for t in m["pricing_tiers"])
        + ". " + m["pricing_note"],
        "- **Demo houses:** " + " · ".join("%s (%s)" % (h["name"], h["status"].split(".")[0])
                                           for h in m["demo_houses"]),
        "",
        "**Known debt:**",
    ]
    for k in m["known_debt"]:
        lines.append("- %s" % k)
    lines.append("")
    lines.append("*Generated from `system/facts.json` by `system/sync.py`. Do not hand-edit this block.*")
    return "\n".join(lines)


BUILDERS = {
    "palette": block_palette,
    "demo-roster": block_demo_roster,
    "dbmedia-summary": block_dbmedia_summary,
}

BLOCK_RE = re.compile(
    r"(<!--\s*AUTO:([a-z0-9\-]+)\s+START\s*-->)(.*?)(<!--\s*AUTO:\2\s+END\s*-->)",
    re.S)

FENCE_RE = re.compile(r"```.*?```", re.S)


def fenced_spans(s):
    """Character ranges inside ``` code fences.

    Documentation that SHOWS an AUTO block (doc-dependencies.md explains the feature) must not be
    treated as a real block, or documenting the tool breaks the tool. Found by the tool itself on
    its first full run, which is a good sign it works."""
    return [(m.start(), m.end()) for m in FENCE_RE.finditer(s)]


def in_fence(pos, spans):
    return any(a <= pos < b for a, b in spans)


def is_frozen(rel):
    if os.path.basename(rel) in FROZEN:
        return True
    return any(fd in rel for fd in FROZEN_DIRS)


def md_files():
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [x for x in dirnames if x not in (".git", "node_modules", "OpenMontage")]
        for fn in filenames:
            if fn.endswith(".md"):
                full = os.path.join(dirpath, fn)
                yield full, os.path.relpath(full, ROOT).replace("\\", "/")


def sync_facts(write):
    d = load()
    drift, wrote, unknown = [], [], []
    for full, rel in md_files():
        if is_frozen(rel):
            continue
        s = io.open(full, encoding="utf-8", errors="replace").read()
        if "<!-- AUTO:" not in s:
            continue
        changed = False
        spans = fenced_spans(s)

        def repl(m):
            name = m.group(2)
            if in_fence(m.start(), spans):
                return m.group(0)
            if name not in BUILDERS:
                unknown.append((rel, name))
                return m.group(0)
            fresh = "\n" + BUILDERS[name](d) + "\n"
            if m.group(3) != fresh:
                drift.append((rel, name))
                return m.group(1) + fresh + m.group(4)
            return m.group(0)

        new = BLOCK_RE.sub(repl, s)
        if new != s:
            changed = True
        if changed and write:
            io.open(full, "w", encoding="utf-8", newline="\n").write(new)
            wrote.append(rel)
    return drift, wrote, unknown


# ---------------------------------------------------------------- link check

PATH_RE = re.compile(r"`([A-Za-z0-9_][A-Za-z0-9_./-]*/[A-Za-z0-9_./-]*)`")
TOP = ("clients", "system", "templates", "docs", "infra", ".claude", "inspiration-library")


def facts_paths(d):
    """Every repo path named in facts.json. These are LOCKED references (hero images, logo dirs,
    source-of-truth docs), so they are checked whatever their extension.

    Added after the demo house hero was moved into a subfolder and the checker said 'all clear':
    the generic doc scan skips .png on purpose (slide renders churn), but a locked hero is the
    opposite of churn. Missing this is exactly the rot the tool exists to catch."""
    out = []

    def walk(v):
        if isinstance(v, dict):
            for k, x in v.items():
                if not k.startswith("_"):
                    walk(x)
        elif isinstance(v, list):
            for x in v:
                walk(x)
        elif (isinstance(v, str) and "/" in v and " " not in v.strip()
              and v.split("/")[0] in TOP):
            out.append(v)
    walk(d)
    return sorted(set(out))


def check_links():
    d = load()
    allow = set(k for k in d.get("_link_check_allowlist", {}) if not k.startswith("_"))
    bad = []
    for cand in facts_paths(d):
        if cand in allow:
            continue
        if not os.path.exists(os.path.join(ROOT, cand)):
            bad.append(("system/facts.json  [LOCKED REFERENCE]", cand))
    for full, rel in md_files():
        if is_frozen(rel):
            continue
        s = io.open(full, encoding="utf-8", errors="replace").read()
        seen = set()
        for m in PATH_RE.finditer(s):
            cand = m.group(1).rstrip("/")
            if cand in seen:
                continue
            seen.add(cand)
            if cand.split("/")[0] not in TOP:
                continue
            if any(t in cand for t in ("*", "[", "YYYY", "...", "NN-")):
                continue
            # Only check things whose absence is a REAL rot signal: documents, folders, and brand
            # assets. Generated content artifacts (slide PNGs, video renders under content/ and
            # assets/) churn constantly by design, and a planned-but-not-yet-made output (the
            # a demo house hero, for instance) is correct to reference before it exists.
            ext = os.path.splitext(cand)[1].lower()
            if ext and ext not in (".md", ".json", ".py", ".html", ".svg"):
                continue
            if "/content/" in cand or "/assets/" in cand:
                continue
            if os.path.exists(os.path.join(ROOT, cand)):
                continue
            if os.path.exists(os.path.join(os.path.dirname(full), cand)):
                continue
            if cand in allow:
                continue
            bad.append((rel, cand))
    return bad


def main():
    args = sys.argv[1:]
    write = "--write" in args
    only_links = "--links" in args
    only_facts = "--facts" in args
    rc = 0

    if not only_links:
        drift, wrote, unknown = sync_facts(write)
        if unknown:
            print("UNKNOWN AUTO BLOCK NAMES (no builder defined):")
            for rel, name in unknown:
                print("   %s -> AUTO:%s" % (rel, name))
            rc = 1
        if write:
            if wrote:
                print("FACTS: rewrote %d file(s):" % len(wrote))
                for r in sorted(set(wrote)):
                    print("   %s" % r)
            else:
                print("FACTS: already in sync, nothing to write.")
        else:
            if drift:
                print("FACTS DRIFT (run: python system/sync.py --write):")
                for rel, name in drift:
                    print("   %s -> AUTO:%s" % (rel, name))
                rc = 1
            else:
                print("FACTS: all AUTO blocks match system/facts.json.")

    if not only_facts:
        bad = check_links()
        if bad:
            print("\nDEAD PATH REFERENCES (%d) in live docs:" % len(bad))
            cur = None
            for f, c in bad:
                if f != cur:
                    print("   %s" % f)
                    cur = f
                print("       -> %s" % c)
            rc = 1
        else:
            print("\nLINKS: every repo path referenced in live docs exists.")

    return rc


if __name__ == "__main__":
    sys.exit(main())
