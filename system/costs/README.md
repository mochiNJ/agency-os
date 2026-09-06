# 💸 Costs — how we track every dollar

This folder is the agency's money tracker: what we spend generating images/videos,
and what we pay in subscriptions. It answers questions like:

- "Slide 1 — how many pictures did we generate and what did they cost in total?"
- "How much has the agency spent this month vs a client?"
- "What are all our subscriptions and what do they add up to per month?"

## The three files (plain English)

| File | What it is | Who edits it |
|---|---|---|
| **`generation-ledger.csv`** | One line per AI image/video we generate (date, brand, which slide, model, cost). | The dispatcher (Claude) appends a line after every generation. You can read/edit it too. |
| **`subscriptions.csv`** | One line per subscription / recurring cost (fal.ai, Canva, Claude, domain…). | You + Claude, whenever a subscription changes. |
| **`SPEND-REPORT.md`** | The pretty, readable summary — totals by brand, by month, by slide, plus subscriptions. **Auto-generated.** | Nobody edits this by hand. A script writes it. |

## How to use it

- **To read your spend:** open **`SPEND-REPORT.md`**. That's the human view.
- **To log a new generation:** add one line to `generation-ledger.csv`, then run:
  ```bash
  python system/costs/rollup.py
  ```
  That recomputes `SPEND-REPORT.md` so the totals are always correct (no hand-math).
- **To update a subscription:** edit `subscriptions.csv`, run the same command.

## The columns

**generation-ledger.csv:** `date, brand, campaign, asset, attempt, model, size, cost_usd, kept, notes`
- `asset` = the thing we're making (e.g. `[product]-slide`). Multiple tries share the same
  `asset` and just increment `attempt` (1, 2, 3…) — that's how "Slide 1 = 3 generations = $X"
  gets grouped automatically.
- `kept` = `y` if we shipped that attempt, `n` if we threw it away, `pending` if not decided.
- `cost_usd` = what that single generation cost. fal shows real usage at fal.ai/dashboard —
  our ledger is our own running record; reconcile against the dashboard monthly.

**subscriptions.csv:** `service, what_it_is, billing, amount_usd, cycle, status, notes`
- `cycle` = `monthly` / `yearly` / `paygo` (pay-as-you-go) / `free`. The report turns yearly
  into a monthly figure so you get one "≈ $X/month" number.
- Rows marked **`CONFIRM`** need real numbers from you (I don't know your Claude plan cost,
  Canva Pro, or your domain registrar fee — tell me and I'll fill them in).

## 🙋 Who keeps this up to date? (so it's never forgotten)

We do NOT rely on anyone "remembering" to log spend. It's built into the tool:

| Layer | Who / what | When |
|---|---|---|
| **Capture** | The fal helper scripts (`infra/fal/fal-image.sh` / `fal-video.sh`) **auto-log every generation** — logging is a side-effect of spending, so it can't be skipped. Cost is estimated from `infra/fal/prices.csv`. | Automatic, every run |
| **Label** | The producing agent (visual-director 08 / video-producer 09) sets `FAL_BRAND` / `FAL_CAMPAIGN` / `FAL_ASSET` / `FAL_KEPT` env vars when it calls the helper, so the row says which brand + slide. | Each generation |
| **Review + reconcile** | **Agent 15 (the Analyst)** — already runs monthly. It reconciles our estimates against the real fal.ai dashboard numbers, fixes drifted prices, and chases any `unlabeled` rows or `CONFIRM` subscriptions. | Monthly |

So: **no separate finance agent.** The tool captures, the producing agent labels, the Analyst reviews.
If you ever see a generation logged as `unlabeled`, an agent forgot to set the env vars — tell me.

To label a generation by hand (or backfill), set the env vars before calling the helper:
```bash
FAL_BRAND=[client] FAL_CAMPAIGN=[product]-flagship FAL_ASSET=[product]-slide FAL_KEPT=y \
  bash infra/fal/fal-image.sh <model> "<prompt>" out.png square_hd
```

## 📏 The two standing rules this enforces (given by the user 2026-08-13)

1. **BEST MODEL FOR THE TASK — price is NEVER the deciding factor.** Better to nail the shot in
   1–2 tries with the top model than burn many tries on a cheap one. Claude picks the right model
   per job (see `infra/fal/README.md`). Cost is recorded here for visibility, NOT to pick a cheaper model.
2. **LOG EVERY GENERATION.** No generation is "done" until its line is in `generation-ledger.csv`
   and the report is regenerated. This is wired into visual-director (08) + video-producer (09).
