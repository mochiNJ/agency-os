# JOB TICKET — [task name]
**Ticket:** system/jobs/YYYY-MM-DD-[client]-[task].md
**Client:** [client-name]
**Requested by user:** [date] — "[short quote of the request]"
**Dispatcher:** main Claude conversation
**Status:** OPEN | BLOCKED | IN PROGRESS | DELIVERED | FAILED

---

## Pipeline stages

Every stage row is filled in by the DISPATCHER, and only after verifying the output file
physically exists (Glob/Read). An agent's own report is not proof. No file = stage not done.

| # | Stage | Agent (spawned?) | Required inputs verified? | Output file (exact path) | File exists? | Time |
|---|-------|------------------|---------------------------|--------------------------|--------------|------|
| 1 | [e.g. copy draft] | copywriter — YES/NO | YES/NO — list checked files | clients/.../pending-humanizer/[file] | ✅/❌ | |
| 2 | [e.g. humanize] | humanizer — YES/NO | | clients/.../pending-qc/[file] | ✅/❌ | |
| 3 | QC review | quality-controller — YES/NO | | system/qc-log.md entry + approved/ or rejected/ | ✅/❌ | |

---

## Input check (stage 0 — before any spawn)

| Required file | Exists? | Notes |
|---------------|---------|-------|
| clients/[name]/brand-profile.md | ✅/❌ | |
| [other CONTRACT inputs of the first agent] | ✅/❌ | |

**If any input is missing → Status: BLOCKED. Report to user. Do not improvise around it.**

---

## QC result

- Score: [X]/10 (min 8) — logged in system/qc-log.md: YES/NO
- Decision: APPROVED / REJECTED (cycle [N] of max 3)
- If rejected — required changes: [copied from QC output]

---

## Delivery

- Final file(s) shown to user: [paths]
- Deviations from protocol (must be empty for a clean run): [none]
