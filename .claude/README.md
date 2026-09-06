# 🤖 `.claude/` — the agents, the skills, and the harness settings

**Charter: what Claude and its sub-agents load. Not a place for client work or for human documentation.**

| | |
|---|---|
| `agents/` | the 16 agent definitions, numbered `01` to `16` to match the pipeline in `CLAUDE.md` |
| `skills/` | installed skill packages, rebuilt by `bash install-skills.sh` |
| `settings.json` | harness settings and hooks, shared |
| `settings.local.json` | this machine's permissions. Not shared. |

---

## `agents/` — every agent file obeys the same three rules

**1. A CONTRACT block, always.** `INPUTS` / `SKILLS` / `HANDOFF` / `OUTPUTS` / `PROOF`. Agents STOP when an
input is missing and are not done until their output files exist. Contracts are enforced, not decorative.

**2. `model: sonnet` in the frontmatter.** Per `system/model-policy.md`, producing and QC sub-agents run on
Sonnet, roughly 5× lighter on the usage limit than Opus. **This was true of only 4 of the 16 agents until
2026-09-06**; the other 12 had no `model:` line and silently inherited the main chat's model, which is the
exact cause of the "one post in two weeks" limit problem the policy was written to prevent. The dispatcher
still spawns a single agent on Opus deliberately when a task is genuinely novel.

**3. A pointer to `system/skill-router.md`, never a re-typed skill list.** The router is the single source
of truth for which skill each agent must load before its first draft.

> **Why that third rule exists.** Until 2026-09-06 **not one of the 16 agents referenced the router**, even
> though both `CLAUDE.md` and the router itself claimed every producing agent read it. Sub-agents spawn with
> no memory and only know what their CONTRACT tells them to read, so the router governed nobody. Agents that
> did name skills had re-typed their own lists, and those lists had drifted: **visual-director never
> mentioned `prompt-engineer`** (mandatory before any image), and paid-ads, influencer and content-strategist
> each missed a mandated skill too. Pointing at one file instead of copying from it is RULE A of
> `system/doc-dependencies.md`, and this is why.

`python system/structure-check.py` fails if an agent is missing `model:`, a CONTRACT block, or the router
pointer.

---

## `skills/` — a skill is only real if `SKILL.md` sits at the top of its folder

A loadable skill is `.claude/skills/<name>/SKILL.md`. A multi-skill repo is `.claude/skills/<repo>/skills/<name>/`
and is namespaced when used (`claude-seo:seo-audit`, `marketing-skills:copywriting`).

**Skills are VENDORED: committed to this repo, so a clone is self-sufficient.** `install-skills.sh` is now
the VERIFIER: it fails loudly if any folder in `skills/` is not loadable, and with `--fetch` it can re-clone
the two packs whose upstream we have actually confirmed. Never clone a skill repo by hand: add it through
that script, so the nested-`SKILL.md` lift happens once and is recorded.

> **Fixed 2026-09-06.** `install-skills.sh` was a 0-byte file while `.gitignore` excluded four skills on the
> promise that it reinstalled them. A fresh clone had no `humanizer` (agent 07's MANDATORY skill, and the
> enforcement point for the global no-em-dash rule) and no `marketingskills` pack. The four are now committed.

> **Why.** Three repos kept their `SKILL.md` one or two levels down, so cloning them verbatim produced
> `creative-director-skill/`, `last30days-skill/` and `x-article-publisher-skill/`: **22 MB of folders Claude
> could never load.** Working copies had been extracted by hand and never written back into the installer, so
> a fresh machine would have silently lacked `creative-director`, which `video-director` **mandates**. The
> installer now takes the subpath explicitly and fails loudly if a skill is not loadable.

Skills not in this folder come from plugins and marketplaces (`anthropic-skills:`, `marketing:`, `postiz:`).
They are not installed by `install-skills.sh` and not stored in this repo.
