# Token Discipline — spend the fewest tokens that still does the job right
**Created 2026-08-18.** Companion to `system/model-policy.md` (which engine) and `system/model-policy.md` (why we were over-spending). This file is the BEHAVIOUR rulebook: it is wired into CLAUDE.md (for the dispatcher) and into every producing/QC agent file (for the agents), and referenced by the PreToolUse hook, so it actually bites — a doc alone does not.

> The rule of thumb: **quality is never the thing we cut. We cut waste** — re-reading files we already know, loose briefs that make an agent re-derive facts, running heavy work in parallel, and doing by an expensive agent what a cheap inline step could do.

## For CLAUDE (the dispatcher)
1. **Read lean.** Never read a whole large file (changelog, progress, agent files can be tens of KB) to get one fact. Use `grep`/targeted `Read` with offset+limit/`tail`. Read the WHOLE file only when you truly need the whole file.
2. **Hand the agent everything it needs, so it doesn't re-read.** A tight, self-contained brief with the exact paths, hexes, copy, and design ids is cheaper than an agent that has to open five files to re-derive them. Every fact you pass = a read the agent skips.
3. **One heavy agent at a time. Never run producing agents in parallel.** Parallel does NOT save total tokens; it just drains the rolling limit twice as fast and trips it mid-work. Sequential is the rule.
4. **Batch.** One QC pass over several finished slides; one agent doing several small fixes — one cold start instead of many.
5. **Do cheap things inline; spawn only for real production.** git, MD edits, file-existence checks, viewing a PNG, small greps — do them yourself. Spawning an agent for those is pure overhead.
6. **Don't re-verify what a tool already confirmed.** Edit/Write error out on failure, so a success means it worked — don't re-Read the file "to check." The harness tracks file state.
7. **Prefer the cheapest correct path.** A cold Sonnet agent is cheaper than resuming a big warm Opus one; a Canva-native fix beats a re-generation; reusing a hosted asset URL beats re-hosting.
8. **Stop when it's right.** Don't add another polish cycle QC didn't ask for.

## For every PRODUCING / QC AGENT (in each agent file)
1. **Read ONLY what your CONTRACT + brief require, and only the part you need.** Targeted `Read` (offset+limit) and `grep`, not full reads of big files. If a fact is already in your brief, do NOT open a file to re-confirm it.
2. **Plan your tool calls before firing.** Avoid redundant screenshots/reads — one verification screenshot at final size, not a series. Don't re-open the same design repeatedly.
3. **One efficient pass.** Make the fix, verify once, hand off. Don't loop re-checking work that's already verified.
4. **Report concisely** — what you did, the output paths, deviations. No re-narrating the whole brief back.
5. **If you're about to do something expensive** (a big generation, a full re-read of a huge file, many screenshots), check it's actually necessary first; if not sure, say so instead of burning the budget.

## The measure
We already saw the win: after these changes, one Sonnet agent did TWO slides in ~145k tokens and a batched QC covered TWO slides in ~137k — each roughly what ONE slide used to cost on Opus. Target: **most of a carousel per limit-window, no mid-work deaths.**
