# NEW CLIENT WORKFLOW — the enforced onboarding SOP ("the boss")

> **Adopted 2026-08-05 (session 30).** This exists because the workflow was correct but scattered across
> CLAUDE.md as prose, and nothing made "no skipping steps" *visible* per client. This file is the single
> gated checklist every new client passes through. **No step may be skipped, ever.** (User rule, session 30.)
>
> This does NOT replace the Dispatcher Protocol or the Agent Pipeline in `CLAUDE.md`; it enforces them.

---

## THE ONE RULE

**A stage cannot start until the previous stage's PROOF FILE physically exists on disk.**
No file = the stage did not happen, regardless of what anyone (client, user, or an agent) reports.
The dispatcher (main Claude) is "the boss": it refuses to advance the client to the next gate until it has
Glob/Read-verified the proof. Skipping, reordering, or "we'll do that later" is a violation. If a client
genuinely doesn't need a stage yet (e.g. SEO before a website exists), it is **PARKED with a written reason
in the client's onboarding tracker** — never silently skipped.

---

## THE GATES (in order — each locked by the one before it)

| Gate | Stage | Agent | PROOF FILE that unlocks the next gate |
|---|---|---|---|
| **G0** | Intake ticket + folder + `creative-decisions-log.md` | dispatcher | `system/jobs/YYYY-MM-DD-[client]-onboarding.md` + `clients/[client]/` + `clients/[client]/creative-decisions-log.md` exist |
| **G1** | Onboarding interview (13 Qs — client answers) | `brand-strategist` | `clients/[client]/brand-profile.md` |
| **G2** | Competitor research (client does nothing) | `competitor-researcher` | `clients/[client]/competitor-report.md` |
| **G3** | Trend research (client does nothing) | `trend-spotter` | `clients/[client]/trend-report.md` |
| **G4** | SEO/AEO audit *(PARK if no live website yet — write the reason)* | `seo-aeo-agent` | `clients/[client]/seo-aeo-report.md` |
| **G5** | 30-day content calendar (needs G1–G3 brain files) | `content-strategist` | `clients/[client]/content-calendar.md` |
| **G6** | Product files — one per product *(PRODUCT brands only)* | dispatcher/strategist | `clients/[client]/products/[product].md` for every product named |
| **G7** | Per-post production | copywriter → humanizer → visual/video | files in `pipeline/pending-qc/` |
| **G8** | Quality gate (min 8/10 + Creative Ambition Gate) | `quality-controller` | entry in `system/qc-log.md` + file in `library/posts/` |
| **G9** | Client creative sign-off (QC pass is NOT approval) | dispatcher → client | user/client "approved" recorded on the ticket |
| **G10** | Publish | `publisher` | live post URL verified on the real profile |
| **G11** | Monthly analysis → feeds back into G2/G3/G5 | `analyst` | report in `clients/[client]/reports/` |

G2, G3, and G4 run **in parallel** (they don't depend on each other, only on G1). Everything else is sequential.

---

## HOW THE DISPATCHER RUNS IT (every new client, no exceptions)

1. **G0** — create the onboarding ticket from `templates/job-ticket-template.md` and the client folder.
   Add the client to `system/active-clients.md` with status `onboarding` and a link to their tracker.
2. Copy the **per-client tracker template** (below) into `clients/[client]/onboarding-status.md`.
   ALSO copy `templates/creative-decisions-log-template.md` into `clients/[client]/creative-decisions-log.md`
   (the running test/feedback record every producing + QC agent reads). Every client gets one from day one.
3. Work the gates **in order**. Before starting any gate, Glob/Read to confirm the previous proof file exists.
4. After each gate, tick it in `clients/[client]/onboarding-status.md` with the proof path + date.
5. Never present a parked gate as "done". Parked = written reason + the trigger that un-parks it.
6. When G1–G5 are green, the client is `active` and normal weekly content production begins.

---

## PER-CLIENT TRACKER TEMPLATE
*(copy into `clients/[client]/onboarding-status.md` at G0)*

```markdown
# Onboarding Status — [Client]
**Started:** YYYY-MM-DD · **Client type:** PRODUCT | SERVICE · **Current gate:** G_

| Gate | Stage | Status | Proof file | Date |
|---|---|---|---|---|
| G0 | Intake ticket + folder | ☐ | | |
| G1 | Onboarding interview | ☐ | brand-profile.md | |
| G2 | Competitor research | ☐ | competitor-report.md | |
| G3 | Trend research | ☐ | trend-report.md | |
| G4 | SEO/AEO audit | ☐ / PARKED | seo-aeo-report.md | |
| G5 | 30-day content calendar | ☐ | content-calendar.md | |
| G6 | Product files (PRODUCT only) | ☐ / N/A | products/*.md | |
| G7+ | Production → QC → sign-off → publish | ☐ | (per piece) | |

**Parked / notes:** _(why any gate is deferred + what un-parks it)_
```

---

## STATUS VALUES
`onboarding` (G0–G1) · `research` (G2–G4) · `planning` (G5) · `active` (G6+) · `paused` · `offboarded`
