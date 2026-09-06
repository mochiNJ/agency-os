#!/usr/bin/env python3
"""
doc-links hook  (PostToolUse: Edit | Write | MultiEdit | NotebookEdit)

Purpose: the moment a GOVERNED file is edited, print the files that must change WITH it.
Backs system/doc-dependencies.md RULE B.

Why it exists: sub-agents spawn fresh with no memory. A rule that says "remember to also update
the calendar" is forgotten by definition. This fires automatically on the edit itself, so
"I didn't know that file existed" stops being possible.

Contract: reads the PostToolUse JSON on stdin, writes hookSpecificOutput.additionalContext on
stdout. ALWAYS exits 0 and never raises: a hook must never block real work.
"""
import sys, os, re, json, fnmatch, datetime

REPO = "C:/Users/kjn/Desktop/AI Agency"
MAP = os.path.join(REPO, "system", "doc-dependencies.md")


def parse_map(path):
    """Parse the [SOURCE]/[WHY]/[DEPENDENT]/[END] blocks into a list of dicts."""
    blocks, cur = [], None
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            line = line.rstrip("\n")
            if line.startswith("[SOURCE]"):
                cur = {"src": line[len("[SOURCE]"):].strip(), "why": "", "deps": []}
            elif cur is None:
                continue
            elif line.startswith("[WHY]"):
                cur["why"] = line[len("[WHY]"):].strip()
            elif line.startswith("[DEPENDENT]"):
                cur["deps"].append(line[len("[DEPENDENT]"):].strip())
            elif line.startswith("[END]"):
                blocks.append(cur)
                cur = None
    return blocks


def relpath(fp):
    """Normalise any absolute/Windows path into a repo-relative posix path."""
    p = fp.replace("\\", "/")
    while "//" in p:
        p = p.replace("//", "/")
    low, repo_low = p.lower(), REPO.lower().rstrip("/") + "/"
    if low.startswith(repo_low):
        p = p[len(repo_low):]
    # NOTE: never lstrip("./") here. It strips CHARACTERS, not a prefix, so a dotfile path
    # like ".claude/agents/x.md" silently became "claude/agents/x.md" and stopped matching.
    if p.startswith("./"):
        p = p[2:]
    return p


# Only tokens that actually WRITE. "sed" alone was a false positive: `sed -n` is read-only and
# fired the hook on every file inspection, which trains everyone to ignore the alert.
_WRITEY = ("sed -i", ">", ">>", "tee ", "cp ", "mv ", "python", "cat <<", "Set-Content", "Out-File")


def _path_from_command(cmd):
    """Best-effort: find a GOVERNED repo file mentioned in a shell command that looks like a write.

    Only fires when the command plausibly writes (sed -i, redirect, tee, cp/mv, python rewrite),
    so read-only greps and cats stay silent. Conservative by design: a missed alert is better
    than crying wolf on every `cat`."""
    if not any(tok in cmd for tok in _WRITEY):
        return ""
    try:
        blocks = parse_map(MAP)
    except Exception:
        return ""
    norm = cmd.replace("\\", "/")
    best = ""
    for m in re.finditer(r'[A-Za-z0-9_./\-]+\.(?:md|json|py|sh)', norm):
        cand = relpath(m.group(0))
        if any(fnmatch.fnmatch(cand, b["src"]) for b in blocks):
            # Prefer the longest match: more specific path wins.
            if len(cand) > len(best):
                best = cand
    return best


def main():
    raw = sys.stdin.read()
    if not raw.strip():
        return
    try:
        data = json.loads(raw)
        tool = data.get("tool_name") or ""
        ti = data.get("tool_input") or {}
        fp = ti.get("file_path") or ""
        cmd = ti.get("command") or ""
    except Exception:
        # Tolerate malformed/unescaped payloads rather than going silent: a hook that
        # quietly stops firing is worse than one that guesses the path.
        tool = ""
        m = re.search(r'"file_path"\s*:\s*"(.+?)"(?=\s*[,}])', raw, re.S)
        fp = m.group(1) if m else ""
        m2 = re.search(r'"command"\s*:\s*"(.+?)"(?=\s*[,}])', raw, re.S)
        cmd = m2.group(1) if m2 else ""

    # Bash/PowerShell edits (sed -i, python rewrite, heredoc, tee, cp) never carry a file_path,
    # so they used to bypass this hook completely. Recover the target from the command text.
    if not fp and cmd:
        fp = _path_from_command(cmd)
    if not fp:
        return

    rel = relpath(fp)
    if not rel or not os.path.exists(MAP):
        return

    hits = [b for b in parse_map(MAP) if fnmatch.fnmatch(rel, b["src"])]
    if not hits:
        return

    today = datetime.date.today().isoformat()
    lines = [
        "LINKED-DOCS ALERT. You just edited a GOVERNED file: %s" % rel,
        "",
        "Per system/doc-dependencies.md RULE B, these dependents must be reconciled in THIS SAME TURN, "
        "before you report done:",
    ]
    for b in hits:
        lines.append("")
        lines.append("  SOURCE %s  (%s)" % (b["src"], b["why"]))
        for d in b["deps"]:
            lines.append("    -> %s" % d)

    lines += [
        "",
        "Do this now:",
        "  1. Open each dependent and check whether your edit just made it wrong or stale.",
        "  2. If it did, fix it in this turn.",
        "  3. If a dependent genuinely cannot be fixed now, paste a stale banner at the TOP of it:",
        "     > WARNING STALE since %s: %s changed. Do not trust this section until reconciled." % (today, rel),
        "     and tell the user which files you left stale and why.",
        "Silently leaving a dependent wrong is the exact failure this rule exists to prevent.",
        "",
        "Prefer RULE A where you can: if the dependent only RESTATES a fact from %s," % rel,
        "replace the copy with a pointer to it, so the two can never drift apart again.",
        "If this edit created, moved, renamed or deleted a file, update PROJECT-MAP.md too.",
        "",
        "STRONGEST OPTION (RULE A+): if this fact is repeated in several live docs, do not hand-copy it.",
        "Put it in system/facts.json and mark each place with an AUTO block, then run:",
        "    python system/sync.py --write",
        "That regenerates every copy from the one value. Run bare 'python system/sync.py' to check for",
        "drift and for dead path references before you commit.",
    ]

    out = {"hookSpecificOutput": {
        "hookEventName": "PostToolUse",
        "additionalContext": "\n".join(lines),
    }}
    sys.stdout.write(json.dumps(out))


try:
    main()
except Exception:
    pass
sys.exit(0)
