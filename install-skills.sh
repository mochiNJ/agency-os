#!/usr/bin/env bash
# install-skills.sh — make sure every skill in .claude/skills/ is present AND loadable.
#
# WHY THIS EXISTS
#   A skill is only real if Claude can load it: SKILL.md must sit at the TOP of the skill's
#   folder (.claude/skills/<name>/SKILL.md), or, for a multi-skill pack, at
#   .claude/skills/<pack>/skills/<name>/SKILL.md. A folder that looks installed but hides its
#   SKILL.md two levels down is a skill that does not exist, and nothing warns you.
#
# WHAT CHANGED (2026-09-06)
#   This file used to be EMPTY, 0 bytes, while .gitignore excluded four skills on the promise
#   that this script reinstalled them. A fresh clone therefore had no `humanizer` (agent 07's
#   MANDATORY skill and the enforcement point for the no-em-dash rule) and no `marketingskills`
#   pack. The skills are now VENDORED: committed to the repo, so a clone is self-sufficient and
#   nothing depends on a third-party repo still being alive.
#
#   So this script no longer installs the common case. It VERIFIES, and it can re-fetch the two
#   packs whose upstream we have actually confirmed, if they ever go missing.
#
# USAGE
#   bash install-skills.sh          # verify every skill is loadable (exit 1 if not)
#   bash install-skills.sh --fetch  # additionally re-clone any confirmed pack that is missing

set -u
cd "$(dirname "$0")" || exit 1
SKILLS=".claude/skills"
FETCH="${1:-}"

# name|upstream|subpath-holding-SKILL.md (empty = repo root). Only CONFIRMED upstreams belong
# here. An unconfirmed URL in an installer is a guess that fails silently on someone else's machine.
FETCHABLE=(
  "claude-seo|https://github.com/AgriciDaniel/claude-seo|"
  "marketingskills|https://github.com/coreyhaines31/marketingskills|"
)

fetch_missing() {
  for row in "${FETCHABLE[@]}"; do
    name="${row%%|*}"; rest="${row#*|}"; url="${rest%%|*}"; sub="${rest#*|}"
    [ -d "$SKILLS/$name" ] && continue
    echo "fetching $name from $url"
    git clone --depth 1 "$url" "$SKILLS/$name" || { echo "  ! clone failed: $name"; continue; }
    rm -rf "$SKILLS/$name/.git"
    if [ -n "$sub" ] && [ -f "$SKILLS/$name/$sub/SKILL.md" ]; then
      # lift the nested skill to the top, or Claude will never see it
      mv "$SKILLS/$name/$sub"/* "$SKILLS/$name/" 2>/dev/null
    fi
  done
}

[ "$FETCH" = "--fetch" ] && fetch_missing

missing=0
for dir in "$SKILLS"/*/; do
  name="$(basename "$dir")"
  if [ -f "$dir/SKILL.md" ]; then
    continue                                   # a plain skill
  fi
  if compgen -G "$dir/skills/*/SKILL.md" > /dev/null; then
    continue                                   # a multi-skill pack, namespaced when used
  fi
  echo "NOT LOADABLE: $name (no SKILL.md at the top, no skills/*/SKILL.md inside)"
  missing=$((missing + 1))
done

total="$(find "$SKILLS" -maxdepth 1 -mindepth 1 -type d | wc -l | tr -d ' ')"
if [ "$missing" -gt 0 ]; then
  echo ""
  echo "$missing of $total skill folders cannot be loaded. Fix the folder shape, or remove it."
  exit 1
fi
echo "OK: all $total skill folders are loadable."
