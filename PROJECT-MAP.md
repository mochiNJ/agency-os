# 🗺 PROJECT MAP — the table of contents for the whole agency

**Purpose:** find any document instantly, and give agents one place to learn where everything lives.
Read `CLAUDE.md` first for the rules; this file is the map.

> ⚠️ **MANDATORY MAINTENANCE RULE: keep this map in sync with reality.** ANY time a file,
> document or folder is **created, moved, renamed or deleted**, update `PROJECT-MAP.md` in the SAME
> turn, as part of that change. It is not done until the map reflects it. This binds every agent and
> the dispatcher alike. A stale map is how things get lost.

> 🆕 **This is a fresh install.** The system is complete; there are no clients yet. Start with
> `system/new-client-workflow.md`.

---

## 🔎 Quick lookup — "where do I find...?"
| I want... | Go to |
|---|---|
| The rules every agent obeys | `CLAUDE.md` (mandates + dispatcher protocol + enforcement) |
| An agent's exact job | `.claude/agents/NN-name.md` (01–16) |
| Which skill an agent MUST load before producing | `system/skill-router.md` |
| How to write image/video prompts | `system/prompt-writing-rules.md` |
| The quality bar / what QC checks | `system/output-quality-rules.md` + `system/qc-rubric.md` |
| Minimum text sizes + how to check legibility | `system/text-size-rules.md` + `python system/preview-at-real-size.py` |
| Where ANY file goes, and when it dies | `system/file-system-law.md` + `system/folder-registry.md`, checked by `python system/structure-check.py` |
| Which files must change TOGETHER when I edit one | `system/doc-dependencies.md` (enforced by the `doc-links` hook in `system/hooks/`) |
| Change a fact ONCE and update every doc | `system/facts.json` + `python system/sync.py --write` |
| How to onboard a new client, gate by gate | `system/new-client-workflow.md` (+ `system/onboarding-questions.md`) |
| A client's identity (palette/fonts) once one exists | `clients/[client]/brand-profile.md` (single source of truth) |
| Reusable visual techniques | `inspiration-library/recipes/` (+ `by-business-type/`) |
| Publishing (Postiz / Instagram / Facebook) | `system/publishing-guide.md` + `infra/postiz/` |
| What each tool cost us | `system/costs/` (`rollup.py` builds `SPEND-REPORT.md`) |
| Which model runs what, and how to spend fewer tokens | `system/model-policy.md` + `system/token-discipline.md` |
| Where every installed tool came from | `system/tool-sources.md` |

---

## 📁 Top-level layout
| Path | What it is |
|---|---|
| `CLAUDE.md` | The operating manual: quality mandates, dispatcher protocol, enforcement rules. |
| `PROJECT-MAP.md` | This file. The index. |
| `.claude/` | `agents/` (16 agent prompts) · `skills/` (vendored, committed) · `settings.json` (the enforcement hooks). |
| `clients/` | One folder per client. Empty on a fresh install. |
| `system/` | The agency's operating files: rules, status, logs, workflow, scripts. |
| `templates/` | Blank templates every new client and job is built from. |
| `docs/` | Setup and reference guides for a human, read once. |
| `inspiration-library/` | Reference material decoded into reusable recipe cards, shared by every client. |
| `dashboard/` | The agency dashboard app (Node). Reads `clients/` live, so it works empty. |
| `infra/` | `fal/` (image + video generation scripts) · `fonts/` · `postiz/` (self-hosted publishing). |
| `.mcp.example.json` | Template for `.mcp.json`. Copy it, fill in your own keys locally. Never commit the real one. |

---

## 🤖 The 16 agents (`.claude/agents/`)
Charter: `.claude/README.md`. Every agent file carries `model: sonnet`, a CONTRACT block
(INPUTS / OUTPUTS / HANDOFF / PROOF), a pointer to `system/skill-router.md`, and the file system law.
`structure-check.py` fails if one is missing.

| # | Agent | Produces |
|---|---|---|
| 01 | brand-strategist | `brand-profile.md` (then triggers 02, 03, 04) |
| 02 | competitor-researcher | `competitor-report.md` |
| 03 | trend-spotter | `trend-report.md` (weekly) |
| 04 | seo-aeo-agent | `seo-aeo-report.md` (quarterly) |
| 05 | content-strategist | `content-calendar.md` |
| 06 | copywriter | copy into `pending-humanizer/` |
| 07 | humanizer | de-AI'd copy into `pending-qc/` (MANDATORY, nothing skips it) |
| 08 | visual-director | images into `pending-qc/` |
| 09 | video-producer | video into `pending-qc/` |
| 10 | campaign-manager | full campaign packages |
| 11 | paid-ads-manager | Meta / Google ad campaigns |
| 12 | email-whatsapp-agent | retention sequences and broadcasts |
| 13 | influencer-agent | discovery, vetting, outreach |
| 14 | publisher | live posts (only from approved work) |
| 15 | analyst | monthly reports, fed back into 03 and 05 |
| 16 | quality-controller | the 8/10 gate + the Creative Ambition Gate |

---

## ⚙️ Scripts you actually run
| Command | What it does |
|---|---|
| `python system/structure-check.py` | Enforces the file system law. Must pass before filing work is called done. |
| `python system/structure-check.py --new-client NAME` | Scaffolds a new client folder correctly. |
| `python system/sync.py` | Checks for fact drift and dead path references (exits non-zero on a problem). |
| `python system/sync.py --write` | Regenerates every AUTO block from `system/facts.json`. |
| `python system/preview-at-real-size.py` | Renders a slide at real feed and grid size to judge legibility. |
| `python system/costs/rollup.py` | Rebuilds the spend report from the generation ledger. |
