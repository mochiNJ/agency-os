# 🗂️ FOLDER REGISTRY

> **Every folder in this repo is listed here with a one-line charter: what belongs in it, and what does
> not.** A folder that is not registered is a folder nobody else will ever find, so
> `python system/structure-check.py` reports unregistered top-level and client folders.
>
> **Creating a folder means adding a row here in the SAME turn** (step 7 of the routing rule in
> `system/file-system-law.md`). The law says *why*; this file says *where*.

---

## TOP LEVEL

| folder | belongs here | does NOT belong here |
|---|---|---|
| `clients/` | one folder per client, each in the canonical shape below | anything about how the agency itself runs |
| `system/` | **everything an AGENT or the dispatcher reads at runtime**: laws, rules, tools, status, history. Charter in `system/README.md`. | client work of any kind, and setup guides a human reads once |
| `docs/` | **what a HUMAN reads, usually once**: setup guides, pricing, parked plans. Charter in `docs/README.md`. | anything an agent reads at runtime. `qc-rubric`, `client-types`, `onboarding-questions` and the publishing guide all lived here wrongly until 2026-09-06 and moved to `system/`. |
| `templates/` | **a blank form to copy and fill in.** Charter in `templates/README.md`. | a filled-in instance, and any dead path: a stale template reproduces the old mess in every new client |
| `infra/` | keys, fonts, containers and scripts that make the tools work. Charter in `infra/README.md`. | client content. Secrets stay gitignored (verified untracked 2026-09-06). |
| `inspiration-library/` | **the ONLY home of reference material**, organised by business type, decoded into reusable moves. Shared by every client. | nothing: there is no per-client board, and creating one is a violation |
| `dashboard/` | our own internal view of `clients/`. Dependency-free Node. Charter in `dashboard/README.md`. | client deliverables, and a second client registry: `system/active-clients.md` is the source of truth, this only holds colours and labels |
| `.claude/` | agent definitions, installed skills, harness settings. Charter in `.claude/README.md`. | client work, and human documentation |
| `.claude/agents/` | the 16 agent files. **Each must carry `model: sonnet`, a CONTRACT block, a pointer to `system/skill-router.md`, and the file system law.** | a re-typed skill list: point at the router instead |
| `.claude/skills/` | installed skill packages, **all COMMITTED since 2026-09-06** so a fresh clone is self-sufficient (the four that used to be fetched were excluded on the promise of a 0-byte installer, which left every clone without `humanizer`). A skill is loadable only when `SKILL.md` sits at the TOP of its folder (or it is a multi-skill repo with `skills/`). | a hand-cloned repo: add it through `install-skills.sh`, which lifts nested skills and verifies loadability |
| `.hermes/skills/` | the SAME skills, at the path the Hermes runtime reads (project-local skills in a git repo). Present only in a checkout built with `python system/export-clean.py --runtime hermes`; never alongside `.claude/skills/` in the same checkout. | a second copy of anything: one checkout serves one runtime |

## INSIDE A CLIENT

| folder | belongs here | does NOT belong here |
|---|---|---|
| *(client root, loose `.md`)* | the brain files: `brand-profile`, `competitor-report`, `trend-report`, `seo-aeo-report`, `content-calendar`, `creative-decisions-log`, `visual-remarks` | any image, any work in progress |
| `brand/` | the CLIENT's own identity assets: `logo/`, fonts, `brand-lock.md`, reusable brand video | research or strategy (brain files), and NOT a product's own identity |
| `products/[product]/` | one folder per product, holding everything about it | anything not tied to a single product |
| `products/[product]/product.md` | every known fact about it. Anything absent is UNKNOWN and is never stated publicly | guesses, invented specs |
| `products/[product]/_inbox/` | **where the user drops files.** Claude empties it the same turn | anything already filed |
| `products/[product]/source-photos/` | real photography supplied by the client, never regenerated | anything AI made |
| `products/[product]/hero/` | the LOCKED reference image everything else is built from | alternates, experiments |
| `products/[product]/worlds/` | generated scenes and frames of the product we chose | rejected or unchosen output |
| `products/[product]/brand/` | **THIS PRODUCT's own identity**: its wordmark, logo, palette board. A demo house is its own brand. | the agency's or the client's logo |
| `products/[product]/_alts/` | correct work we did not choose (LAW 2). Names say the direction | anything WRONG, that gets deleted |
| `pipeline/` | **IN MOTION only.** Drains to empty at the end of every job | finished work |
| `pipeline/_inbox/` | client-level drops not tied to one product | product assets |
| `pipeline/pending-humanizer/` | copy written, awaiting the Humanizer | images |
| `pipeline/pending-qc/` | built, awaiting Agent 16 | anything already scored |
| `pipeline/pending-signoff/` | passed QC, awaiting the client. **QC is not sign-off** | anything not yet QC'd |
| `library/posts/YYYY-MM-DD-slug/` | **AT REST.** One post: its slides, its caption, its `post.md` manifest | work still in motion |
| `campaigns/[campaign]/` | a **time-boxed programme across several posts AND at least one non-social channel** (ads, email, influencer): the brief, the budget, the cross-channel pieces, and LINKS to its posts | product identity, and the post files themselves. Both belong elsewhere. If you are hesitating between this and a product, **it is the product**. |
| `prompts/` | **append-only.** Every image and video prompt, verbatim | anything rewritten later |
| `qc-notes/` | **append-only.** QC verdicts and the lessons in them | live work |
| `reports/` | monthly analyst output and audits | raw data |
| `website/` | this client's site, IF one exists. the agency's was deleted 2026-09-06 (retired the agency brand, broken paths, and the recorded decision was that a future site starts fresh rather than patching it). | content for social |
| `video-project/` | Remotion source. **Follows JS conventions, not ours** | finished renders that belong to a post |

## THE TWO UNDERSCORE FOLDERS, AND ONLY THESE TWO

`_inbox/` (just arrived, not filed) and `_alts/` (correct, not chosen). Anything else starting with `_`
is a violation and `structure-check.py` fails on it. **There is no `_archive/`: git is the archive.**

## EVERY GOVERNED FOLDER CARRIES ITS OWN CHARTER

`clients/`, `system/`, `docs/`, `templates/`, `inspiration-library/` and each client folder must hold a
`README.md` saying what belongs in them and what does not. `structure-check.py` fails when one is missing.
A folder whose rules live only in someone's head is a folder that drifts.

## NAMING EXEMPTIONS (deliberate, not oversights)

Source code and vendored assets follow **their own** conventions, because forcing ours on them would break
imports and font lookups. `ClientReel.jsx` and `Orbitron-Bold.ttf` are correctly named. Exempt from the
naming checks: `*/video-project/`, `*/website/`, `dashboard/`, `infra/`, `templates/`.

Build-output directories (`video-project/public/`) may hold a copy of a source asset, because the bundler
can only read from there. Exempt from the duplicate check.
