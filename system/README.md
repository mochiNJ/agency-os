# ⚙️ `system/` — how the agency runs

**Charter: everything an AGENT or the dispatcher needs at runtime. No client work, ever.**
If it is about one client, it belongs in that client's folder. If a human reads it once during setup,
it belongs in `docs/`.

> Full rules: [`file-system-law.md`](file-system-law.md) · every folder's charter:
> [`folder-registry.md`](folder-registry.md) · check the repo: `python structure-check.py`

## THE LAW AND ITS ENFORCEMENT
| file | what it is |
|---|---|
| `file-system-law.md` | **where every file lives, what its status is, when it dies.** Read before filing anything. |
| `folder-registry.md` | one-line charter for every folder in the repo |
| `structure-check.py` | enforces the law. Must pass before filing work is called done. |
| `doc-dependencies.md` | which files must change together (RULE A point-don't-copy, RULE B propagate) |
| `facts.json` + `sync.py` | change a shared fact ONCE; `sync.py --write` regenerates every copy |
| `hooks/doc-links.py` | the PostToolUse hook that prints dependents on every edit |

## RULES AGENTS OBEY
| file | what it governs |
|---|---|
| `prompt-writing-rules.md` | image and video prompts (RULE 0, RULE 7, prompt visibility) |
| `output-quality-rules.md` | the living quality bar QC enforces |
| `text-size-rules.md` | **the only source of type sizes.** Never re-type a px value elsewhere. |
| `qc-rubric.md` | the full QC scoring rubric |
| `skill-router.md` | which skill each agent must load before producing |
| `model-policy.md` · `token-discipline.md` | which model, and how not to waste the usage limit |
| `font-pipeline.md` | why text renders locally and Canva stays for vector work |
| `client-types.md` · `onboarding-questions.md` · `new-client-workflow.md` | onboarding |
| `publishing-guide.md` | how publishing actually works, read before any publish |

## CURRENT STATE (edit in place, never append)
`active-clients.md` (the client register) · `pipeline-status.md` · `next-session-prompt.md` (ONE handoff)
· `weekly-trends.md`

## APPEND-ONLY HISTORY (never rewritten, even when paths inside go stale)
`changelog.md` · `progress.md` · `qc-log.md` · `verified-facts.md` · `jobs/` · `costs/`

**The difference matters.** A "current state" file that gets appended to becomes a log, and then nobody
can tell what is true now. That is exactly what happened to `pipeline-status.md` (63 stacked blocks) and
`next-session-prompt.md` (21 stacked handoffs) before 2026-09-06.
