# 🔗 DOC DEPENDENCIES — which files must change TOGETHER

**Why this file exists (user, 2026-09-05):** documents in this repo are linked. When one is edited, the
change often *must* also land in another file. Agents are spawned fresh with no memory, so they never
knew the second file existed. Result: two files, two different answers, and the older one silently wins
the next time an agent reads it. (Real case: `demo-products/README.md` still taught "composite the label
onto a blank product" for a month after RULE 0 replaced it, and the content calendar stamped the agency's
own palette onto a fragrance house whose spec file forbids exactly that.)

---

## THE TWO RULES

**RULE A — POINT, DON'T COPY (prevention, always preferred).**
A fact has exactly ONE home. Every other file *references* that home instead of restating it.
Never re-type a palette hex, a font name, a price, a product spec, or a locked URL into a second file:
write `see clients/[client]/products/[product]/product.md → LOCKED IDENTITY` instead.
A fact that lives in one place cannot go out of sync. This rule removes the problem; Rule B only manages it.

**RULE A+ — GENERATE IT (the strongest form, added 2026-09-05).**
When a fact is repeated in several LIVE documents and pointing is not enough (a status table a human needs to
read at a glance, for instance), do not hand-maintain the copies. Put the fact in **`system/facts.json`** and
mark each place it appears with an AUTO block:

```
*(generated block: add the fact to `system/facts.json`, mark the spot with an AUTO block, then run `python system/sync.py --write`)*
```

Then `python system/sync.py --write` rewrites every block from the one value. Change it once, everywhere
updates. This exists because the user measured the pain honestly: the agency palette was restated in 26
files, demo-house status in 20, pricing in 9. RULE B (propagate by hand) manages that; RULE A+ removes it.
`python system/sync.py` with no flags CHECKS instead of writing, and also verifies that every repo path named
in a live doc still exists, so a moved file cannot quietly leave dead references behind.

**RULE B — PROPAGATE IN THE SAME TURN (when duplication is genuinely unavoidable).**
If you edit a SOURCE file below, you update its DEPENDENTS in the SAME turn, before you report done.
The `doc-links` hook prints the dependent list automatically every time you edit a governed file, so
"I didn't know" is not available. If a dependent genuinely cannot be updated now, you MUST paste a
stale banner at the very top of that dependent and tell the user:
`> ⚠️ STALE since YYYY-MM-DD: [source file] changed ([what]). Do not trust [which section] until reconciled.`
Leaving a dependent silently wrong is the failure this file exists to prevent.

**Conflict resolution:** the SOURCE always wins. If a dependent disagrees with its source, the dependent
is the bug. Fix the dependent, never "reconcile" by editing the source to match a stale copy.

---

## THE MAP
<!-- MACHINE-READ: system/hooks/doc-links.sh greps [SOURCE] blocks. Keep the exact tag format. -->

[SOURCE] system/file-system-law.md
[WHY] Where every file lives, what its status is, and when it dies. Binds every agent and every filing decision.
[DEPENDENT] system/structure-check.py | the checker must enforce exactly what the law says, no more and no less
[DEPENDENT] system/folder-registry.md | every folder the law names needs a charter row
[DEPENDENT] CLAUDE.md | the FOLDER STRUCTURE block
[DEPENDENT] PROJECT-MAP.md | the layout tables and the quick-lookup row
[DEPENDENT] .claude/agents/*.md | the FILE SYSTEM LAW block inside each CONTRACT
[DEPENDENT] system/sync.py | its FROZEN_DIRS must match the law's append-only history list
[END]

[SOURCE] system/file-system-law.md  (folder moves)
[WHY] Code reads repo folders. A move that skips the code leaves a silently broken app while the checkers say clean.
[DEPENDENT] dashboard/server.js | it walks clients/ live; its paths ARE the structure
[DEPENDENT] system/structure-check.py | its ABOLISHED_PATHS / ABOLISHED_SEGMENTS lists
[END]

[SOURCE] system/active-clients.md
[WHY] The register of who is a client and what state they are in.
[DEPENDENT] dashboard/server.js | its REGISTRY block is DISPLAY ONLY and must not contradict the register
[DEPENDENT] system/pipeline-status.md | the per-client stage rows
[END]

[SOURCE] system/skill-router.md
[WHY] The single source of truth for which skill each agent loads before producing. Until 2026-09-06 not one agent pointed at it, so it governed nobody.
[DEPENDENT] .claude/agents/*.md | each CONTRACT must POINT at the router, never re-type its own skill list
[DEPENDENT] CLAUDE.md | the MAXIMUM QUALITY MANDATE references it
[END]

[SOURCE] system/model-policy.md
[WHY] Which model each agent runs on. Sonnet is ~5x lighter on the usage limit than Opus.
[DEPENDENT] .claude/agents/*.md | every agent needs `model: sonnet` in its frontmatter, or it silently inherits Opus
[DEPENDENT] .claude/README.md | the agent rules restated for whoever opens that folder
[END]

[SOURCE] install-skills.sh
[WHY] Rebuilds .claude/skills on a fresh machine. If it installs to a path where SKILL.md is nested, the skill silently does not exist.
[DEPENDENT] .claude/README.md | the loadability rule
[DEPENDENT] system/skill-router.md | it must not mandate a skill the installer cannot produce
[END]

[SOURCE] system/structure-check.py
[WHY] The enforcement. A rule it does not check is a rule that does not exist.
[DEPENDENT] system/file-system-law.md | a new check, or a new exemption, must be written into the law
[DEPENDENT] system/folder-registry.md | the naming/duplicate exemption list
[END]

[SOURCE] clients/*/brand-profile.md
[WHY] Single source of truth for a client's name, palette, fonts, tagline, channels.
[DEPENDENT] clients/*/visual-remarks.md | any palette/font rule restated there
[DEPENDENT] clients/*/content-calendar.md | palette hexes or fonts quoted inside image prompts
[DEPENDENT] clients/*/brand/logo/README.md | logo colourways must match the live palette
[DEPENDENT] clients/*/campaigns/*/BRAND-LOCK.md | campaign locks inherit the brand palette
[DEPENDENT] PROJECT-MAP.md | only if the client's identity summary line changed
[END]

[SOURCE] clients/[client]/products/*.md
[WHY] The LOCKED IDENTITY of a demo house. Every post about that house inherits it.
[DEPENDENT] clients/[client]/content-calendar.md | every post spec naming this house (palette, label, hero path, product description)
[DEPENDENT] clients/[client]/products/README.md | the status table row (identity status, hero image path)
[DEPENDENT] clients/[client]/prompts/*.md | saved prompts that describe this product
[DEPENDENT] clients/[client]/campaigns/*/ | any campaign built on this house
[END]

[SOURCE] clients/[client]/products/README.md
[WHY] Teaches the demo-product PIPELINE. If the pipeline changes, the rule files must agree.
[DEPENDENT] system/prompt-writing-rules.md | RULE 0 must not contradict this README
[DEPENDENT] clients/[client]/visual-remarks.md | the stage list restated for the agency visuals
[DEPENDENT] templates/demo-product-identity-kit.md | the kit must produce what the pipeline consumes
[END]

[SOURCE] clients/[client]/prompts/*-post-prompts.md
[WHY] The slide map for one specific post/carousel: which generated image fills which slide, and which
generated images are spares, pending-swap, or rejected.
[DEPENDENT] clients/[client]/products/[house]/README.md | the per-house asset index must show the
same used / spare / rejected status for every file this slide map names
[DEPENDENT] system/jobs/*-post-prompts.md | the job ticket's stage table must match the slide map's resolved/pending state
[END]

[SOURCE] system/prompt-writing-rules.md
[WHY] The canonical prompt/production rules every producing agent obeys.
[DEPENDENT] .claude/agents/08-visual-director.md | its GATEs must reflect the current rules
[DEPENDENT] .claude/agents/09-video-producer.md | same
[DEPENDENT] .claude/agents/16-quality-controller.md | QC must test what the rules require
[DEPENDENT] clients/[client]/products/README.md | must not teach a retired method
[DEPENDENT] system/output-quality-rules.md | overlapping quality rules must agree
[END]

[SOURCE] clients/*/content-calendar.md
[WHY] The production plan. Status and scheduling live elsewhere.
[DEPENDENT] system/pipeline-status.md | what is planned / in production / live
[DEPENDENT] clients/*/creative-decisions-log.md | if a post was changed due to user feedback
[END]

[SOURCE] clients/*/campaigns/*/BRAND-LOCK.md
[WHY] A campaign's absolute source of truth, above the brief and above memory.
[DEPENDENT] clients/[client]/products/[product]/slide-tracker.md | for the demo brand flagship: per-slide status + rules
[DEPENDENT] clients/[client]/products/[product]/product.md | the house identity must match its campaign lock
[DEPENDENT] clients/*/content-calendar.md | the post spec for this campaign
[END]

[SOURCE] .claude/agents/*.md
[WHY] An agent's CONTRACT. Changing what an agent reads/produces changes the pipeline.
[DEPENDENT] PROJECT-MAP.md | the agent reference table
[DEPENDENT] system/skill-router.md | the mandatory skill for that agent
[DEPENDENT] CLAUDE.md | only if the pipeline order or a mandate changed
[END]

[SOURCE] CLAUDE.md
[WHY] The operating manual. A rule here binds every agent.
[DEPENDENT] PROJECT-MAP.md | structure/index must reflect it
[DEPENDENT] .claude/agents/*.md | a new hard rule must be wired into the agents it binds
[DEPENDENT] .claude/settings.json | if the rule needs hook enforcement to actually bite
[END]

[SOURCE] clients/*/creative-decisions-log.md
[WHY] Where user creative feedback is recorded. Feedback that stays here alone never reaches an agent.
[DEPENDENT] system/prompt-writing-rules.md | if the feedback is a standing production rule
[DEPENDENT] system/output-quality-rules.md | if it is a quality bar
[DEPENDENT] clients/*/visual-remarks.md | if it is client-specific visual guidance
[END]

[SOURCE] templates/client-folder-structure.md
[WHY] What a new client's folders contain.
[DEPENDENT] system/new-client-workflow.md | the gated SOP must create what the template defines
[DEPENDENT] CLAUDE.md | the FOLDER STRUCTURE block
[DEPENDENT] PROJECT-MAP.md | the layout tables
[END]

---

## ALWAYS-ON (no matter which file changed)
- **Any** file created, moved, renamed, archived or deleted → `PROJECT-MAP.md`, same turn. (Existing mandate.)
- **Any** substantive change → `system/changelog.md` + `system/progress.md` before the session closes.
- **Any** QC run → `system/qc-log.md`. No entry = the deliverable does not exist.

## ADDING A NEW LINK
When you notice two files that must move together, add a `[SOURCE]` block here in the same turn.
This map is only as good as it is current, and it is cheaper to add a link than to debug a contradiction.
