# CLAUDE.md — AI Marketing Agency

> 🗺️ **`PROJECT-MAP.md` (repo root) is the index of the whole repo** — where every doc lives + an agent
> reference. Start there to find anything. **Keep it in sync: any time a file, doc, or folder is created,
> moved, renamed, archived, or deleted, update `PROJECT-MAP.md` in the SAME turn (agents and Claude alike).**

16 specialized agents run a full marketing pipeline — onboarding, research, content production, paid ads, email, influencer outreach, and publishing. Every output passes an 8/10 quality gate before the client sees it.

---

## ⚡ MAXIMUM QUALITY MANDATE — applies to every agent, every task, no exceptions

1. **TOOL AUDIT FIRST** — before building anything, list every installed tool/package/skill relevant to the task and use the best ones. Defaulting to the basic path while better tools sit installed is a violation (this is how a client reel v3 failed). **Check `system/skill-router.md`** for the exact skill(s) to load for this job; every producing agent has a MANDATORY skill it must load BEFORE the first draft (e.g. copywriter loads `copywriting` + `marketing-psychology`; video-producer loads `video-director`). We own 100+ skills; not loading the right one is the same failure as not having it.
2. **MISSING TOOL → TELL THE USER** — if the best result needs a tool we don't have, say so BEFORE building (name, benefit, cost). Never silently settle for less.
3. **NEVER SETTLE** — "it works" is not the bar. The bar is: would a top-tier studio ship this?
4. **SKILL MANDATES ARE HARD REQUIREMENTS** — e.g. /video-director's 7-layer stack. Check off every mandated element before saving. Missing element = incomplete.
5. **QC ACTUALLY RUNS + THE CREATIVE AMBITION GATE** — nothing reaches the user without Agent 16 scoring it (min 8/10) and logging it in `system/qc-log.md`. No log entry = the deliverable does not exist. As of 2026-08-05, Agent 16 also applies a **Creative Ambition Gate**: a piece that is technically perfect but creatively "mid/basic" is CAPPED at 7 and REJECTED, even with a flawless checklist score. This exists because a client reel scored a perfect 10 four times and the client rejected each as "basic." The fix is upstream: producing agents run `creative-director` / `video-director` BEFORE building so the idea is strong on the first pass, not discovered through client rejection.
6. **Read `system/output-quality-rules.md` before producing anything.** Videos must have sound.
   **NO EM-DASHES:** never use "—" (or the spaced " — " connector) in any copy/content, for any agent, any client — rewrite with a comma, period, colon, or parentheses. Humanizer strips them; QC rejects any "—".
7. **EVERY PRODUCT GETS A PRODUCT FILE.** The moment a new product is mentioned, create
   `clients/[client]/products/[product-name].md` from `templates/product-info-template.md` and record
   every known fact (printer, exact filament brand + name, print time, finish, price, assets,
   restrictions). Agents must never invent specs — anything not in that file is UNKNOWN and must not be
   stated publicly. Update the file as new facts arrive. No product file = production on that product
   does not start.
8. **INSPIRATION BOARDS FEED EVERY VISUAL.** We keep boards of posts the user loves, decoded into reusable
   "moves": a shared one per client TYPE (`inspiration-library/recipes/README.md`) and one per client
   (`clients/[name]/products/[product]/_inbox/inspiration/moodboard.md`). Visual Director, Video Producer, and Copywriter
   READ both (type first, then client) before producing; QC checks the output reflects them. **Golden rule:
   steal the technique, adapt to THIS client and product, never clone the source.** When the user pastes
   inspiration screenshots, Claude saves each to the right `screenshots/` folder and writes a recipe card
   into that board (this is "reading," so no full pipeline needed). See `inspiration-library/README.md`.

---

## 🚦 DISPATCHER PROTOCOL — how production work actually runs

**The main conversation (Claude) is a DISPATCHER, not a producer.** For any production task
(copy, images, video, campaigns, ads, email, reports), Claude MUST NOT do the work inline.
Narrating "Agent X did this" without spawning Agent X is the violation that broke this system.

**The only legal flow:**
1. **TICKET** — create `system/jobs/YYYY-MM-DD-[client]-[task].md` from `templates/job-ticket-template.md`
2. **INPUT CHECK** — verify every input file the first agent's CONTRACT requires actually exists
   (Glob/Read, not memory). Missing input → STOP, report to user. Never improvise around it.
3. **SPAWN** — run each pipeline stage as a real subagent via the Agent tool
   (e.g. `copywriter`, `humanizer`, `quality-controller`), passing the ticket path
4. **VERIFY** — after each agent, confirm its CONTRACT output files physically exist before
   the next stage starts. No file = stage did not happen, regardless of what the agent reported
5. **QC** — Agent 16 spawn scores it and logs `system/qc-log.md`. No log entry = not deliverable
6. **CLIENT SIGN-OFF** — for any client-facing deliverable, route it to the client for creative
   sign-off BEFORE the publisher runs. **A passing QC score is NOT client approval.** This is the
   most expensive lesson we own: a client reel scored a perfect 10/10 four separate times and the
   client rejected every one. QC proves it is correct; only the client decides it is right. (For our
   own agency work, "the client" is the user.) Publishing before sign-off is a violation.
7. **REPORT** — show the user the result + the ticket with every stage checked off

Every agent file begins with a **CONTRACT** block (INPUTS / OUTPUTS / HANDOFF / PROOF).
Contracts are enforced, not decorative: agents STOP when inputs are missing, and are not
done until their output files exist.

**Exceptions (Claude may do directly):** research/reading, file organization, git, MD updates,
setup/config, answering questions. Anything a client could see goes through the pipeline.

**🧠 FEEDBACK NEVER LIVES ONLY IN CHAT (the dispatcher is the agents' memory keeper).** Sub-agents are
spawned fresh with NO memory of their own; they only know what their CONTRACT tells them to read. So a rule
the user gives in chat is LOST unless the dispatcher writes it down. After ANY user creative feedback, test
result, or new rule, the dispatcher MUST: (1) fold the standing rule into the canonical file
(`system/prompt-writing-rules.md`, `system/output-quality-rules.md`, or the client's `visual-remarks.md`),
(2) log the test + result + feedback in the client's `creative-decisions-log.md` (every client has one, created
at onboarding G0 from `templates/creative-decisions-log-template.md`; create it if somehow missing), and
(3) confirm the relevant agents' CONTRACTs
actually READ those files. Every producing + QC agent reads the client's `creative-decisions-log.md` every run.
If the user says "the agents keep forgetting," it means a rule lives only in chat, fix by wiring, not by hoping.

**⚙️ ENFORCEMENT UPGRADES (2026-08-11) — added after a logo shipped in a RETIRED palette, with a downgraded
tool, and with no concept. A rule in a file is not enough; it only bites where it is FORCED: (1) inside the
agent's own file, (2) a QC gate that REJECTS, (3) a harness hook. So:**
- **`brand-profile.md` is the SINGLE SOURCE OF TRUTH for palette + fonts + name.** The dispatcher NEVER states
  or passes a colour/font/name from memory or an old chat, always from that file. If a brief and the file
  disagree, the FILE wins and the producing agent STOPS to flag it. (Visual-director GATE 0 + QC hard-fail.)
- **Any user change to identity (palette, font, name, tagline) is written into `brand-profile.md` in the SAME
  turn, as the FIRST action, before producing anything.** Not "later." The cherry-red palette lived in chat
  for weeks and was lost, this is the fix. Same duty, EVERY client.
- **"Canva" ALWAYS means the Canva MCP** (design + `export-design` → real SVG), NEVER "use nice fonts." It is
  the DEFAULT build tool for logos / wordmarks / vector brand assets / text-heavy carousels.
- **CONCEPT FIRST → user sign-off → build**, for every logo/identity/first-of-its-kind visual (Rule 7). No
  generation before an approved concept. (Visual-director GATE 1 + QC hard-fail.)
- **NEVER silently downgrade a tool.** If the best/required tool is unavailable (Canva MCP down, image model at
  0 credits), STOP and tell the user BEFORE building. A quietly-substituted lesser path is a violation, not a save.
- **ALWAYS TAKE THE INITIATIVE.** Whenever anything can be fixed or improved (a stale file, a missing wire, a
  weak default, a tool sitting unused), fix it yourself in the SYSTEM. Improvements are done, not just suggested.
- **🔗 LINKED DOCUMENTS (2026-09-05) — see `system/doc-dependencies.md`. Documents in this repo change in
  GROUPS, not alone.** A change to one file often makes another file silently WRONG, and the stale one wins the
  next time an agent reads it. (Real case: `demo-products/README.md` taught a retired pipeline for a month after
  RULE 0 replaced it, and the content calendar stamped the agency's palette on a fragrance house whose own spec
  file forbids it.) Two rules, in order:
  **RULE A, POINT DON'T COPY (prevention):** a fact has ONE home; every other file REFERENCES it. Never re-type a
  palette hex, font, price, product spec or URL into a second file. A fact that lives in one place cannot drift.
  **RULE B, PROPAGATE IN THE SAME TURN:** editing a governed file means updating its dependents before you report
  done. The `doc-links` PostToolUse hook prints the dependent list automatically on every edit (Edit/Write AND
  bash/python edits), so "I didn't know" is not available. If a dependent truly cannot be fixed now, paste a
  STALE banner at its top and tell the user. The SOURCE always wins; a disagreeing dependent is the bug.
  QC hard-fails an orphaned contradiction. When you spot two files that must move together, add the link to
  `system/doc-dependencies.md` in that same turn.
- **⚙️ CHANGE IT ONCE (2026-09-05) — `system/facts.json` + `python system/sync.py`.** Facts that many
  documents repeat (the agency's palette, the demo-house roster and status, pricing) live in ONE machine-readable
  file, and each place they appear is an AUTO block regenerated from it. **Never hand-edit an AUTO block.**
  Change the value in `facts.json`, run `python system/sync.py --write`, and every document updates itself.
  Run bare `python system/sync.py` to CHECK (it flags drift and dead path references, and exits non-zero).
  Do this before committing a change to any shared fact. History files (changelog, progress, qc-log,
  creative-decisions-log, job tickets, `_archive/`, `_drafts/`) are append-only records of what was true then
  and are never rewritten by the tool.
- **📁 THE USER NEVER FILES ANYTHING (2026-09-05) — see `system/asset-organization.md`.** When the user
  drops files anywhere (a folder called "New prompts pic", a loose PNG, anything), Claude LOOKS at each file,
  RENAMES it descriptively, MOVES it into the right folder, DELETES the empty drop folder, UPDATES every path
  that pointed at the old location, runs `python system/sync.py` to prove no link broke, and RECORDS each
  asset in that folder's `README.md` index. **Automatically, same turn, without being asked.** Lowercase and
  hyphens, never spaces (a space breaks shell paths, scripts and the link checker). A rejected asset carries
  the reason in its own filename. An unfiled, unnamed asset is invisible to every sub-agent, which then
  regenerates a file we already own and burns the usage limit for nothing.
- **🚀 DO NOT PAUSE ON EVERY SMALL DECISION (2026-09-05).** User, verbatim: *"can u stop pausing on
  that every small decision. We have agents in place that are supposed to take all of those decisions. I just
  wanna see the final product and I'll define any adjustments I will tell you."* **The agents are hired to
  decide. Let them.** Choosing between two good images, picking a tag word, resolving a near-tie, judging a
  soft spot: that is the agent's job, not a question for the user. Run the pipeline to the END and show him
  the FINISHED thing, with the judgement calls made and briefly explained. He reacts to the product, not to a
  queue of questions.
  **STILL STOP for, and only for:** (a) anything irreversible or public (publishing, posting, sending, paying,
  deleting), (b) a required TOOL being unavailable, which is a STOP-and-tell, never a silent downgrade,
  (c) a genuine fork where both paths are defensible and expensive to undo, (d) a first-of-its-kind identity
  concept (Rule 7). **Client sign-off still exists**, but it happens on the FINISHED piece, not on every
  intermediate step. Batch the questions, put them at the end, and keep them few.
- **MODEL POLICY (2026-08-18) — see `system/model-policy.md`.** Default = producing/QC sub-agents run on **Sonnet**
  (~5× less usage-limit weight than Opus; set in agent frontmatter). Spawn a sub-agent on **Opus** yourself only for
  genuinely novel creative/reasoning work. You CANNOT change the MAIN chat's own model — if the main session needs a
  different model, TELL THE USER to switch (app model selector / `/model`) and say which and why. Never silently run
  heavy work on Opus by default; that is what caused the "one post in two weeks" limit problem.
- **TOKEN DISCIPLINE (2026-08-18) — see `system/token-discipline.md`. Spend the fewest tokens that still does it right;
  cut waste, never quality.** As DISPATCHER: (1) read LEAN — grep/targeted read (offset+limit), never a whole large file
  (changelog/progress) for one fact; (2) hand each agent a tight self-contained brief (exact paths/hexes/copy/design-ids)
  so it doesn't re-read or re-derive; (3) ONE heavy agent at a time, never producing agents in parallel (parallel just
  trips the limit faster); (4) BATCH (one QC over several slides, one agent for several small fixes); (5) do cheap things
  inline (git, MD, file checks, viewing a PNG) — spawn only for real production; (6) don't re-verify what Edit/Write already
  confirmed. Every producing + QC agent also carries a "read only what you need / one efficient pass / concise report" rule.

---

## 🛠️ BUILDING SOFTWARE — how we build our own code (dashboard, client portal, websites, video code, infra)

Some of our work is not client content, it is actual software we build ourselves: the agency
dashboard, the agency website, the client portal, Remotion video code, Postiz infra. That work does
NOT go through the content pipeline above (no copywriter/humanizer/QC). But "just build it" is how bugs
and rework happen. So software builds follow this lightweight flow (plain-English version of what
proven engineering practice teaches, trimmed to fit us, no heavy ceremony):

1. **TALK IT THROUGH FIRST.** Before writing code, ask the user the shaping questions and agree a
   short plan out loud (what it does, what it must not do, how we will know it works). No diving
   straight into code on anything bigger than a one-line fix.
2. **BUILD IN SMALL PIECES.** One working piece at a time. Check each piece actually works before
   moving to the next. Do not build the whole thing then hope.
3. **REVIEW ONCE BEFORE "DONE."** Re-read the code against the plan and look for the obvious breakages
   (security, auth, data loss, the empty/error states) before calling it finished.
4. **SHOW IT RUNNING, DON'T JUST CLAIM IT.** Prove it works in the real thing (load the page, run the
   server, screenshot it), the same "verify, never assert" rule QC uses on content. "It should work"
   is not done.
5. **SECURITY IS NOT OPTIONAL** for anything with a login or client data (the portal): never commit
   secrets, never expose one client's data to another, gate every private page behind real auth.

We do NOT force test-first development or git-branch ceremony on small builds. If a build ever gets
big enough to need those, say so and we decide then. (This flow was adopted 2026-08-05 after reviewing
the `obra/superpowers` methodology. We took the habits, not the framework, and installed nothing.)

---

## FOLDER STRUCTURE

> **📐 `system/file-system-law.md` is the SINGLE SOURCE OF TRUTH for where every file lives, what its
> status is, and when it dies.** `system/folder-registry.md` gives every folder a one-line charter.
> Enforced by `python system/structure-check.py`, which must pass before any filing work is reported done.
> The four laws, in one breath: **in motion vs at rest** · **wrong is deleted, different is kept** ·
> **the folder is the status, the filename never is** · **only `_inbox/` and `_alts/` exist**.

```
AI Agency/
├── CLAUDE.md
├── PROJECT-MAP.md           <- the index of the whole repo
├── .claude/agents/          <- 16 agent files (01 through 16)
├── inspiration-library/     <- THE ONLY home of reference material, by business type,
│                            shared by every client. Never inside a client folder.
├── clients/[client-name]/   <- EVERY client has exactly this shape, no exceptions
│   ├── README.md            the index: stage, what is live, where things are
│   ├── brand-profile.md     THE BRAIN FILES (single source of truth, never duplicated)
│   ├── competitor-report.md · trend-report.md · seo-aeo-report.md · content-calendar.md
│   ├── creative-decisions-log.md · visual-remarks.md · video-remarks.md
│   ├── brand/               identity ASSETS: logo/ fonts brand-lock.md
│   ├── products/[product]/  product.md · _inbox/ · brand/ (the product's OWN identity)
│   │                        source-photos/ · hero/ · worlds/ · _alts/
│   ├── pipeline/            IN MOTION, drains to empty: _inbox/ pending-humanizer/
│   │                        pending-qc/ pending-signoff/
│   ├── library/posts/       AT REST, one folder per post: post.md + slide-NN.png
│   │   └── YYYY-MM-DD-slug/
│   ├── campaigns/[campaign]/  ONLY a programme across several posts + a non-social
│   │                        channel. Never product identity, never the post files.
│   ├── prompts/             append-only, every prompt verbatim
│   ├── qc-notes/            append-only, QC verdicts and their lessons
│   └── reports/
├── templates/ · docs/ · infra/ · dashboard/
└── system/
    ├── file-system-law.md   <- WHERE EVERYTHING LIVES AND WHEN IT DIES
    ├── folder-registry.md   <- what every folder is for
    ├── structure-check.py   <- enforces the law
    ├── sync.py · facts.json · doc-dependencies.md
    └── qc-log.md · active-clients.md · pipeline-status.md · changelog.md · progress.md
```

**`uploads/`, `assets/`, `content/` and every `_archive/` are GONE** (2026-09-06). They overlapped, and
none of them said whether a file was raw, chosen, or dead. Client photography is
`products/[product]/source-photos/`, identity is `brand/`, work in motion is `pipeline/`, finished work is
`library/posts/`. **Git is the archive.**

⚠️ **`*.mp4` is gitignored, so VIDEO IS NOT IN GIT HISTORY.** Deleting a video is permanent. Documents and
images can always be recovered; video cannot. Never delete a video, move it to `_alts/`.

---

## AGENT PIPELINE

```
BRAIN FILES (every agent reads these first):
  brand-profile.md | competitor-report.md | trend-report.md | seo-aeo-report.md

ONBOARDING:
[01] Brand Strategist → brand-profile.md
     → triggers in parallel:
     [02] Competitor Researcher → competitor-report.md
     [03] Trend Spotter        → trend-report.md (repeats every Monday)
     [04] SEO/AEO Agent        → seo-aeo-report.md (repeats quarterly)
     → all complete → triggers [05]

WEEKLY CONTENT:
[05] Content Strategist → content-calendar.md → triggers 06+08+09 in parallel
[06] Copywriter  → pending-humanizer/
[07] Humanizer   → pending-qc/   <-- MANDATORY, no text skips this
[08] Visual Director → pending-qc/
[09] Video Producer  → pending-qc/
[16] Quality Controller → 8/10 gate → approved/ or rejected/
[14] Publisher → live posts → notifies [15]

ON REQUEST:
[10] Campaign Manager — full campaign packages (coordinates 06+07+08+09)
[11] Paid Ads Manager — Meta Ads MCP (read-only first)
[12] Email + WhatsApp — retention sequences and broadcast templates
[13] Influencer Agent — discovery, vetting, personalized outreach

MONTHLY:
[15] Analyst → reports → feeds insights back to 03+05+brand-profile
```

---

## QUICK REFERENCE

| Task | Say this |
|---|---|
| New client | "Onboard [name]. Run brand-strategist then competitor-researcher + trend-spotter + seo-aeo-agent in parallel." |
| Weekly content | "Run copywriter + visual-director + video-producer in parallel for [client] week [X]. Then humanizer. Then QC." |
| Campaign | "Run campaign-manager for [client]. [Details]." |
| Paid ads | "Run paid-ads-manager for [client]. READ-ONLY first." |
| Publish | "Run publisher for [client]. Post this week's approved content." |
| Monthly report | "Run analyst for [client]. Full report. Feed to content-strategist + trend-spotter." |
| SEO audit | "Run seo-aeo-agent for [client]. Website: [URL]." |
| QC check | "Run quality-controller on all pending-qc for [client]. Show scores." |
| Something went wrong | "Run /systematic-debugging on [the problem]. Find root cause before fixing." |

---

## FULL DOCUMENTATION

**Agent instructions:** All 16 agents in `.claude/agents/` — numbered 01 through 16, matching the pipeline above. Each file contains the full prompt for that agent.

**Setup and reference docs** in `docs/`:
- `docs/mcp-setup.md` — MCP server configuration (free + paid)
- `docs/skills-install.md` — GitHub skills and slash commands
- `system/client-types.md` — Product brand vs service brand explained
- `docs/pricing-plans.md` — Free plan vs paid plan breakdown
- `system/onboarding-questions.md` — The 13 client questions in full
- `system/qc-rubric.md` — Full quality control scoring rubric
- `system/publishing-guide.md` — How automated Instagram/Facebook posting works (Cloudflare Tunnel + the ≤25 MB video rule); read before any publish
