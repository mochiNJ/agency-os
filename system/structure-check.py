#!/usr/bin/env python3
"""
structure-check.py - enforces system/file-system-law.md

A rule only bites where it is forced. This is the force.

Run bare to CHECK (exits non-zero if the repo breaks the law):
    python system/structure-check.py

Show every offending file rather than a sample:
    python system/structure-check.py --all

Only one area:
    python system/structure-check.py --only duplicates
"""

import argparse
import hashlib
import io
import os
import re
import sys
import time
from collections import defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ---------------------------------------------------------------- exclusions

# Third-party, generated, or vendored. Not ours, not our problem.
EXCLUDE_DIR_NAMES = {
    ".git", "node_modules", "__pycache__", ".venv", "venv",
    ".next", "dist", "build", ".dashboard", "OpenMontage",
}
# A skill folder lives under one of these, depending on which agent runtime this
# checkout serves: Claude Code reads .claude/skills/, Hermes reads .hermes/skills/.
# Both are checked the same way, so one repo can serve either runtime.
SKILL_ROOTS = (".claude/skills", ".hermes/skills")

EXCLUDE_PREFIXES = (
    ".claude/skills/",      # vendored skill packs, verified by install-skills.sh
                            # (their CONTENTS are third-party; the folders themselves
                            #  are still checked for loadability)
    ".hermes/skills/",      # the same skills when this checkout serves Hermes
    ".claude/plugins/",
    "infra/bin/",           # downloaded tools
    "dashboard/node_modules/",
    "_archive/Antigravity/",  # frozen pre-agency scratch, kept as-is
)

# Append-only history. Records what was true at the time; never rewritten.
# Exempt from NAMING rules only. Still checked for duplicates and stray folders.
HISTORY_PREFIXES = (
    "system/jobs/",
    "system/qc-log.md",
    "system/changelog.md",
    "system/progress.md",
    "system/agency-audit",
    "system/system-upgrade-audit",
    "system/usage-optimization-audit",
)
HISTORY_PATTERNS = (
    re.compile(r"^clients/[^/]+/prompts/"),
    re.compile(r"^clients/[^/]+/creative-decisions-log\.md$"),
    re.compile(r"^clients/[^/]+/qc-notes/"),
)

# Source code and vendored assets follow THEIR OWN conventions, not ours.
# ClientReel.jsx and Orbitron-Bold.ttf are correctly named; forcing our naming
# rules onto them would break imports and font lookups. A rule that flags correct
# work is a bad rule, so these are exempt from the NAMING checks only.
CODE_PATTERNS = (
    re.compile(r"^clients/[^/]+/video-project/"),
    re.compile(r"^clients/[^/]+/website/"),
    re.compile(r"^dashboard/"),
    re.compile(r"^infra/"),
    re.compile(r"^templates/"),
)

# Build-output directories legitimately hold a copy of a source asset, because
# the bundler can only read from them. Exempt from the DUPLICATE check.
BUILD_ASSET_PATTERNS = (
    re.compile(r"^clients/[^/]+/video-project/public/"),
    re.compile(r"^dashboard/public/"),
)

# ---------------------------------------------------------------- the law

# LAW 3: the folder is the status, the name never says status.
# NOTE: "copy" is deliberately NOT banned. In a marketing agency "copy" means the
# written words (copy-onslide.md), which is core vocabulary. Actual duplicate files
# are caught authoritatively by the content-hash check, not by guessing from a name.
BANNED_NAME_TOKENS = [
    "final", "old", "superseded", "approved", "rejected", "retired",
    "draft", "temp", "tmp", "untitled",
]
BANNED_RE = re.compile(
    r"(?:^|[-_. ])(" + "|".join(BANNED_NAME_TOKENS) + r")(?:$|[-_. ])",
    re.IGNORECASE,
)
# A trailing "-v2" or "(1)" used as a version stamp.
# Deliberately does NOT match a bare "-01": the law endorses zero-padded numbered
# sets (slide-01, world-02) and date suffixes (-2026-09-06), which are not statuses.
VERSION_STAMP_RE = re.compile(r"(?:-v\d+|\(\d+\))(?=\.[A-Za-z0-9]+$)")

# LAW 4: exactly two underscore folders exist.
LEGAL_UNDERSCORE_DIRS = {"_inbox", "_alts"}

# The canonical client shape.
# NOTE: "inspiration" is deliberately ABSENT. Reference material lives in
# inspiration-library/[business-type]/ so every client can use it. A per-client
# board fragments the library and duplicates it (see the law, LAW 1 section).
LEGAL_CLIENT_DIRS = {
    "brand",          # the CLIENT's own identity assets: logo, fonts, brand-lock
    "products",       # one folder per product
    "pipeline",       # IN MOTION, drains to empty
    "library",        # AT REST, finished work grouped by post
    "campaigns",      # multi-post programmes
    "prompts",        # append-only, every prompt verbatim
    "qc-notes",       # append-only, QC verdicts and their lessons
    "reports",        # monthly analyst output
    "website",        # this client's site, if we build one
    "video-project",  # Remotion source, if this client has video
}
LEGAL_PIPELINE_DIRS = {
    "_inbox", "pending-humanizer", "pending-qc", "pending-signoff",
}
LEGAL_PRODUCT_DIRS = {
    "_inbox", "_alts", "source-photos", "hero", "worlds",
    "brand",   # a demo house is its own brand: its wordmark, palette board, logo
}
LEGAL_TOP_DIRS = {
    "clients", "system", "docs", "templates", "infra",
    "inspiration-library", "dashboard", ".claude", ".hermes", "_archive",
}

# Files whose whole job is to say WHAT IS TRUE NOW. If one grows past its cap it has
# stopped being a status and become a log, and then nobody can tell what is current.
# Caps set 2026-09-06, after pipeline-status.md reached 618 lines (63 stacked dated
# blocks) and next-session-prompt.md reached 1135 lines (21 stacked handoffs, the top
# one the only live instruction). History goes to changelog.md / progress.md instead.
CURRENT_STATE_CAPS = {
    "system/pipeline-status.md": 150,
    "system/next-session-prompt.md": 400,
    "system/active-clients.md": 120,
    "system/weekly-trends.md": 200,
}

# Folders that must carry a README charter saying what belongs in them.
NEED_CHARTER = ("system", "docs", "templates", "inspiration-library", "clients",
                ".claude", "infra", "dashboard")

# Every agent file must carry these. Checked 2026-09-06 after finding that only 4 of
# 16 agents had a model line (the other 12 silently inherited Opus, against
# system/model-policy.md) and that NOT ONE of the 16 referenced system/skill-router.md,
# so the router that both CLAUDE.md and the router itself claimed every agent reads
# was in fact governing nobody.
AGENT_REQUIRED = [
    ("model: sonnet", "no `model:` line: it inherits the main chat's model, against "
                      "system/model-policy.md. Spawn on Opus deliberately, never by default."),
    ("## CONTRACT", "no CONTRACT block: INPUTS / SKILLS / HANDOFF / OUTPUTS / PROOF"),
    ("skill-router", "does not point at system/skill-router.md, so it will never load "
                     "its mandated skill"),
    ("FILE SYSTEM LAW", "does not carry the file system law block"),
]

# A file in motion for longer than this is a stalled job, not a queue entry.
PIPELINE_STALE_DAYS = 14

MEDIA_EXT = {".png", ".jpg", ".jpeg", ".webp", ".svg", ".gif", ".mp4", ".mov", ".pdf"}


# ---------------------------------------------------------------- helpers

def rel(path):
    return os.path.relpath(path, ROOT).replace(os.sep, "/")


def is_excluded(relpath):
    return relpath.startswith(EXCLUDE_PREFIXES)


def is_code(relpath):
    return any(p.search(relpath) for p in CODE_PATTERNS)


def is_build_asset(relpath):
    return any(p.search(relpath) for p in BUILD_ASSET_PATTERNS)


def is_history(relpath):
    if relpath.startswith(HISTORY_PREFIXES):
        return True
    return any(p.search(relpath) for p in HISTORY_PATTERNS)


def walk_files():
    """Yield (abspath, relpath) for every file we actually govern."""
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if d not in EXCLUDE_DIR_NAMES]
        r = rel(dirpath)
        if r != "." and is_excluded(r + "/"):
            dirnames[:] = []
            continue
        for fn in filenames:
            ap = os.path.join(dirpath, fn)
            rp = rel(ap)
            if is_excluded(rp):
                continue
            yield ap, rp


def walk_dirs():
    for dirpath, dirnames, _ in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if d not in EXCLUDE_DIR_NAMES]
        r = rel(dirpath)
        if r == ".":
            continue
        if r in SKILL_ROOTS:
            # yield the skill folders themselves, but do not descend into their
            # third-party contents
            for d in sorted(dirnames):
                yield os.path.join(dirpath, d), r + "/" + d
            dirnames[:] = []
            continue
        if is_excluded(r + "/"):
            dirnames[:] = []
            continue
        yield dirpath, r


def sha(path):
    h = hashlib.sha256()
    try:
        with open(path, "rb") as f:
            for chunk in iter(lambda: f.read(1 << 20), b""):
                h.update(chunk)
    except OSError:
        return None
    return h.hexdigest()


# ---------------------------------------------------------------- checks

def check_names(files):
    """LAW 3: no status words, no version stamps in filenames."""
    out = []
    for ap, rp in files:
        if is_history(rp) or is_code(rp):
            continue
        name = os.path.basename(rp)
        stem = os.path.splitext(name)[0]
        hit = BANNED_RE.search(stem)
        if hit:
            out.append((rp, 'name says status: "%s"' % hit.group(1)))
        elif "/_alts/" in rp:
            # Nothing in _alts/ is current, so a number there identifies an
            # iteration rather than claiming a status.
            continue
        elif VERSION_STAMP_RE.search(name):
            out.append((rp, "name carries a version stamp"))
    return out


def check_paths(files):
    """LAW 3 naming: lowercase-with-hyphens, no spaces."""
    out = []
    for ap, rp in files:
        if is_code(rp):
            continue
        if " " in rp:
            out.append((rp, "path contains a space (breaks scripts and sync.py)"))
        elif re.search(r"[A-Z]", os.path.basename(rp)) and not rp.endswith(".md"):
            out.append((rp, "filename has uppercase letters"))
    return out


def check_underscore_dirs(dirs):
    """LAW 4: only _inbox/ and _alts/ exist."""
    out = []
    for ap, rp in dirs:
        base = os.path.basename(rp)
        if base.startswith("_") and base not in LEGAL_UNDERSCORE_DIRS:
            if rp == "_archive" or rp.startswith("_archive/"):
                continue  # reported separately, it is being abolished
            out.append((rp, "illegal underscore folder (only _inbox/ and _alts/ exist)"))
    return out


def check_client_shape(dirs):
    """Every client has the same shape. No client invents its own."""
    out = []
    for ap, rp in dirs:
        parts = rp.split("/")
        if parts[0] != "clients":
            continue
        if len(parts) == 2:
            continue  # the client folder itself
        if len(parts) == 3:
            d = parts[2]
            if d not in LEGAL_CLIENT_DIRS and not d.startswith("_"):
                out.append((rp, "not part of the canonical client shape"))
        if len(parts) == 4 and parts[2] == "pipeline":
            if parts[3] not in LEGAL_PIPELINE_DIRS:
                out.append((rp, "not a legal pipeline queue"))
        if len(parts) == 5 and parts[2] == "products":
            if parts[4] not in LEGAL_PRODUCT_DIRS:
                out.append((rp, "not a legal product sub-folder"))
    return out


def check_top_level(dirs):
    out = []
    for ap, rp in dirs:
        if "/" in rp:
            continue
        if rp not in LEGAL_TOP_DIRS:
            out.append((rp, "unregistered top-level folder (add it to system/folder-registry.md)"))
    return out


def check_duplicates(files):
    """The same bytes must not exist in two places."""
    by_hash = defaultdict(list)
    for ap, rp in files:
        if os.path.splitext(rp)[1].lower() not in MEDIA_EXT:
            continue
        if is_build_asset(rp):
            continue
        try:
            if os.path.getsize(ap) == 0:
                continue
        except OSError:
            continue
        h = sha(ap)
        if h:
            by_hash[h].append(rp)
    out = []
    for h, paths in by_hash.items():
        if len(paths) > 1:
            out.append((paths[0], "identical to: " + ", ".join(paths[1:])))
    return out


def check_pipeline_drain(files):
    """LAW 1: a queue that is not empty at the end of a job is a bug."""
    out = []
    cutoff = time.time() - PIPELINE_STALE_DAYS * 86400
    for ap, rp in files:
        if "/pipeline/" not in rp:
            continue
        if os.path.basename(rp) in ("README.md", ".gitkeep"):
            continue
        try:
            mtime = os.path.getmtime(ap)
        except OSError:
            continue
        if mtime < cutoff:
            age = int((time.time() - mtime) / 86400)
            out.append((rp, "stalled in a queue for %d days (should have drained)" % age))
    return out


def check_archive(dirs):
    """LAW 4: there is no _archive/. Git is the archive."""
    out = []
    for ap, rp in dirs:
        base = os.path.basename(rp)
        if base in ("_archive", "_superseded", "_retired", "_drafts", "_rejected", "_raw"):
            if rp.startswith("_archive/Antigravity"):
                continue
            n = sum(len(f) for _, _, f in os.walk(ap))
            out.append((rp, "abolished graveyard folder (%d files). Git is the archive." % n))
    return out


def check_registered_clients(dirs):
    """A client folder nobody registered is either a mistake or invisible.

    Added 2026-09-06 after a scaffold test (clients/acme-widgets) was left behind
    and no check caught it, because "an extra client" was structurally legal.
    """
    try:
        reg = io.open(os.path.join(ROOT, "system", "active-clients.md"),
                      encoding="utf-8").read()
    except OSError:
        return []
    out = []
    for ap, rp in dirs:
        parts = rp.split("/")
        if len(parts) != 2 or parts[0] != "clients":
            continue
        if parts[1] not in reg:
            out.append((rp, "client folder is not listed in system/active-clients.md "
                            "(a stray scaffold, or a client nobody registered)"))
    return out


def check_no_client_inspiration(dirs):
    """Reference material lives in inspiration-library/, never inside a client."""
    out = []
    for ap, rp in dirs:
        parts = rp.split("/")
        if len(parts) >= 3 and parts[0] == "clients" and parts[2] == "inspiration":
            out.append((rp, "inspiration belongs in inspiration-library/[business-type]/, "
                            "outside the clients, so every client can use it"))
    return out


def check_placeholder_dirs(dirs):
    """A .gitkeep that became a DIRECTORY, and folders holding nothing at all."""
    out = []
    for ap, rp in dirs:
        base = os.path.basename(rp)
        if base in (".gitkeep", ".keep"):
            out.append((rp, "a placeholder FILE was turned into a directory (bad move/rename)"))
            continue
        try:
            entries = os.listdir(ap)
        except OSError:
            continue
        if not entries:
            out.append((rp, "empty folder: either fill it, or delete it"))
        elif entries == [".gitkeep"] and "/pipeline/" not in rp + "/" and not rp.endswith("/posts"):
            out.append((rp, "holds only a .gitkeep: delete it until it is actually needed"))
    return out


def check_status_not_log(files):
    """A status file that is appended to instead of edited becomes a log."""
    out = []
    for rp, cap in CURRENT_STATE_CAPS.items():
        ap = os.path.join(ROOT, rp.replace("/", os.sep))
        if not os.path.exists(ap):
            continue
        n = sum(1 for _ in io.open(ap, encoding="utf-8", errors="replace"))
        if n > cap:
            out.append((rp, "%d lines, cap is %d. This file says WHAT IS TRUE NOW: edit it in "
                            "place. Put history in system/changelog.md and system/progress.md."
                        % (n, cap)))
    return out


def check_charters(dirs):
    """A folder with no README is a folder whose rules live only in someone's head."""
    out = []
    for ap, rp in dirs:
        if rp not in NEED_CHARTER and not (rp.startswith("clients/") and rp.count("/") == 1):
            continue
        if not os.path.exists(os.path.join(ap, "README.md")):
            out.append((rp, "no README.md: every governed folder states its own charter"))
    return out


def check_agents(files):
    """Every agent obeys the same three rules. See .claude/README.md."""
    out = []
    for ap, rp in files:
        if not rp.startswith(".claude/agents/") or not rp.endswith(".md"):
            continue
        s = io.open(ap, encoding="utf-8", errors="replace").read()
        for needle, why in AGENT_REQUIRED:
            if needle not in s:
                out.append((rp, why))
    return out


def check_skills_loadable(dirs):
    """A skill is only real when SKILL.md sits at the TOP of its folder.

    Added 2026-09-06 after three repos were cloned verbatim with SKILL.md nested one
    or two levels down: 22 MB of folders Claude could never load, while a fresh
    machine would silently lack creative-director, which video-director mandates.
    """
    out = []
    for ap, rp in dirs:
        parts = rp.split("/")
        if len(parts) != 3 or parts[0] + "/" + parts[1] not in SKILL_ROOTS:
            continue
        if os.path.exists(os.path.join(ap, "SKILL.md")):
            continue
        if os.path.isdir(os.path.join(ap, "skills")):
            continue  # multi-skill repo, namespaced when used
        out.append((rp, "no SKILL.md at its top level and no skills/ folder: the agent "
                        "cannot load this. Check it with install-skills.sh, which also "
                        "lifts a nested SKILL.md."))
    return out


# Folder names abolished by the file system law. If one of these appears in CODE, the
# code is reading a path that no longer exists.
#
# Added 2026-09-06 after dashboard/server.js kept reading uploads/logo and
# content/approved for a full restructure, so every client silently rendered with no
# logo and zero assets. sync.py never saw it because it only link-checks .md files.
# A checker that reports "clean" while the app is broken is worse than no checker.
# Folder names abolished by the file system law. If one of these appears in CODE, the
# code is reading a path that no longer exists.
#
# Added 2026-09-06 after dashboard/server.js kept reading uploads/logo and
# content/approved through a full restructure, so every client silently rendered with
# no logo and zero assets. sync.py never saw it because it only link-checks .md files.
# A checker that reports "clean" while the app is broken is worse than no checker.
#
# TWO forms are needed, and the first version of this check only had one, so it MISSED
# the very bug it was written for: real code says path.join(dir, 'uploads', 'logo'),
# where the string "uploads/logo" never appears. Segments must be matched too.
ABOLISHED_PATHS = [
    # These are the abolished CLIENT sub-folders, listed explicitly.
    # A bare "uploads/" was tried and reverted on 2026-09-06: it false-positived on
    # Postiz's own /uploads docker volume and on a code comment describing this very
    # rule. A check that flags correct work gets switched off, so precision matters
    # more than reach here.
    "uploads/portfolio", "uploads/logo", "uploads/product-photos", "uploads/inspiration", "uploads/brand-assets",
    "content/approved", "content/published", "content/rejected",
    "content/pending-qc", "content/pending-humanizer",
    "assets/images", "assets/videos", "demo-products",
]
# quoted single segments, e.g. path.join(base, 'uploads')
ABOLISHED_SEGMENTS = ["uploads", "demo-products", "_superseded", "_retired",
                      "_drafts", "_rejected"]
SEGMENT_RE = re.compile(
    r"""['"](%s)['"]""" % "|".join(re.escape(x) for x in ABOLISHED_SEGMENTS))

CODE_EXT = {".js", ".py", ".sh", ".bat", ".ps1", ".html", ".jsx", ".ts", ".tsx", ".yml", ".yaml"}

# The same abolished folders, written RELATIVELY inside a live document
# ("slides/reveal.png", "uploads/logo", "content/approved"). sync.py cannot see these:
# it only validates paths that begin with a top-level folder, so a relative one is
# invisible. 17 files were carrying them after the 2026-09-06 restructure, including
# the gated onboarding SOP and three templates, which between them would have taught
# every FUTURE client the abolished structure. Found by hand; now checked.
RELATIVE_ABOLISHED = re.compile(
    r"(?:^|[^a-zA-Z0-9/_.-])(slides|uploads|assets|demo-products|content)/[a-z0-9._*\[-]")
# These name the abolished folders on purpose, in order to forbid or explain them.
DOC_ALLOW = ("system/file-system-law.md", "system/folder-registry.md", "templates/README.md",
             "docs/README.md", "system/README.md", "clients/README.md", ".claude/README.md",
             "dashboard/README.md", "infra/README.md", "inspiration-library/README.md")


def check_doc_paths(files):
    """A live document must not point at a folder the law abolished."""
    out = []
    for ap, rp in files:
        if not rp.endswith(".md") or is_history(rp) or rp in DOC_ALLOW:
            continue
        if "/_alts/" in rp or any(rp.startswith(r + "/") for r in SKILL_ROOTS):
            continue
        try:
            text = io.open(ap, encoding="utf-8", errors="replace").read()
        except OSError:
            continue
        for line in text.splitlines():
            if "http://" in line or "https://" in line:
                continue
            m = RELATIVE_ABOLISHED.search(line)
            if m:
                out.append((rp, 'points at "%s/", a folder the law abolished' % m.group(1)))
                break
    return out


def check_code_paths(files):
    """Code must not read a folder the law abolished."""
    out = []
    for ap, rp in files:
        if os.path.splitext(rp)[1].lower() not in CODE_EXT:
            continue
        if rp.startswith(("system/structure-check.py", "system/sync.py")):
            continue  # these two NAME the abolished folders in order to police them
        try:
            text = io.open(ap, encoding="utf-8", errors="replace").read()
        except OSError:
            continue
        hit = None
        for line in text.splitlines():
            if "example.com" in line or "http://" in line or "https://" in line:
                continue  # a URL path, not a repo path
            for bad in ABOLISHED_PATHS:
                if bad in line:
                    hit = bad
                    break
            if hit:
                break
            m = SEGMENT_RE.search(line)
            if m:
                hit = m.group(1)
                break
        if hit:
            out.append((rp, 'reads "%s", a folder the law abolished. '
                            "See system/file-system-law.md." % hit))
    return out


CHECKS = [
    ("names",       "LAW 3  filenames must not carry status",      check_names,            "files"),
    ("paths",       "LAW 3  lowercase-with-hyphens, no spaces",    check_paths,            "files"),
    ("underscore",  "LAW 4  only _inbox/ and _alts/ exist",        check_underscore_dirs,  "dirs"),
    ("archive",     "LAW 4  no graveyard folders, git is history", check_archive,          "dirs"),
    ("shape",       "SHAPE  every client has the same folders",    check_client_shape,     "dirs"),
    ("toplevel",    "SHAPE  top-level folders are registered",     check_top_level,        "dirs"),
    ("clients",     "SHAPE  every client folder is registered",    check_registered_clients, "dirs"),
    ("inspiration", "SHAPE  inspiration lives outside the clients", check_no_client_inspiration, "dirs"),
    ("empty",       "SHAPE  no empty or placeholder-only folders", check_placeholder_dirs, "dirs"),
    ("charters",    "DOCS   every governed folder has a README",   check_charters,         "dirs"),
    ("status",      "DOCS   status files stay status, not logs",   check_status_not_log,   "files"),
    ("agents",      "AGENT  model + contract + router + law",       check_agents,           "files"),
    ("skills",      "AGENT  every skill folder is loadable",        check_skills_loadable,  "dirs"),
    ("code",        "CODE   no code reads an abolished folder",     check_code_paths,       "files"),
    ("docpaths",    "DOCS   no doc points at an abolished folder",  check_doc_paths,        "files"),
    ("duplicates",  "LAW 1  the same bytes live in one place",     check_duplicates,       "files"),
    ("pipeline",    "LAW 1  queues drain to empty",                check_pipeline_drain,   "files"),
]


BRAIN_FILES = ["brand-profile.md", "competitor-report.md", "trend-report.md",
               "seo-aeo-report.md", "content-calendar.md", "creative-decisions-log.md",
               "visual-remarks.md"]


def scaffold(name):
    """Create a new client in the canonical shape. Never build one by hand."""
    base = os.path.join(ROOT, "clients", name)
    if os.path.exists(base):
        print("clients/%s already exists. Nothing done." % name)
        return 1
    dirs = ["brand/logo", "inspiration/screenshots", "products", "campaigns",
            "prompts", "qc-notes", "reports", "library/posts",
            "pipeline/_inbox", "pipeline/pending-humanizer",
            "pipeline/pending-qc", "pipeline/pending-signoff"]
    for d in dirs:
        os.makedirs(os.path.join(base, d), exist_ok=True)
        open(os.path.join(base, d, ".gitkeep"), "w").close()
    stub = (
        "# {title}\n\n"
        "> Not yet written. Fill this in via the gated SOP in\n"
        "> system/new-client-workflow.md. Until then this client is NOT ready\n"
        "> for production, and agents must STOP rather than improvise.\n"
    )
    for f in BRAIN_FILES:
        with open(os.path.join(base, f), "w", encoding="utf-8") as fh:
            fh.write(stub.format(title=f[:-3]))
    with open(os.path.join(base, "README.md"), "w", encoding="utf-8") as fh:
        fh.write(
            "# {n}\n\n"
            "**Stage:** scaffolded, not onboarded.\n\n"
            "Shape defined by `system/file-system-law.md`. Drop files in any `_inbox/`;\n"
            "Claude names and files them.\n".format(n=name)
        )
    print("created clients/%s in the canonical shape" % name)
    print("next: run the gated SOP in system/new-client-workflow.md")
    return 0


def main():
    ap = argparse.ArgumentParser(description="Enforce system/file-system-law.md")
    ap.add_argument("--new-client", metavar="NAME",
                    help="scaffold a new client in the canonical shape, then exit")
    ap.add_argument("--all", action="store_true", help="list every offender, not a sample")
    ap.add_argument("--only", help="run one check by name")
    args = ap.parse_args()

    if args.new_client:
        return scaffold(args.new_client)

    files = list(walk_files())
    dirs = list(walk_dirs())

    print("=" * 74)
    print(" STRUCTURE CHECK   %d files, %d folders governed" % (len(files), len(dirs)))
    print(" law: system/file-system-law.md")
    print("=" * 74)

    total = 0
    for key, title, fn, kind in CHECKS:
        if args.only and args.only != key:
            continue
        findings = fn(files if kind == "files" else dirs)
        findings.sort()
        if not findings:
            print("\n  [ok]   %s" % title)
            continue
        total += len(findings)
        print("\n  [FAIL] %s" % title)
        print("         %d violation(s)" % len(findings))
        shown = findings if args.all else findings[:8]
        for path, why in shown:
            print("           %s" % path)
            print("               -> %s" % why)
        if len(findings) > len(shown):
            print("           ... and %d more (run with --all)" % (len(findings) - len(shown)))

    print("\n" + "=" * 74)
    if total:
        print(" RESULT: %d violation(s). The repo breaks the file system law." % total)
        print(" Fix them, or if a rule is genuinely wrong, change the law and say why.")
        print("=" * 74)
        return 1
    print(" RESULT: clean. Every file obeys the law.")
    print("=" * 74)
    return 0


if __name__ == "__main__":
    sys.exit(main())
