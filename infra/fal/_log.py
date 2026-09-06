#!/usr/bin/env python3
"""Auto-log one fal generation to the spend ledger, then regenerate the report.

Called BY fal-image.sh / fal-video.sh on every successful generation, so a spend
can never be forgotten (logging is a side-effect of spending). Not usually run by
hand. Reads context from env vars (all optional except model):

  LOG_MODEL   the fal model id (required)
  LOG_SIZE    image size / video length label
  FAL_BRAND   e.g. [client]        (default: unlabeled)
  FAL_CAMPAIGN e.g. [product]-flagship
  FAL_ASSET   e.g. [product]-slide  (attempts on the same asset auto-group)
  FAL_KEPT    y / n / pending      (default: pending)
  FAL_NOTES   free text

Cost is estimated from infra/fal/prices.csv (fal doesn't return a per-call price).
Reconcile against fal.ai/dashboard monthly. Unknown model -> cost left blank but
the spend event is STILL recorded. Stdlib only.
"""
import csv, os, sys, subprocess, datetime

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", ".."))
LEDGER = os.path.join(REPO, "system", "costs", "generation-ledger.csv")
PRICES = os.path.join(HERE, "prices.csv")
ROLLUP = os.path.join(REPO, "system", "costs", "rollup.py")

model = os.environ.get("LOG_MODEL", "").strip()
if not model:
    sys.stderr.write("_log.py: LOG_MODEL not set; skipping ledger write\n")
    sys.exit(0)

size = os.environ.get("LOG_SIZE", "").strip()
brand = os.environ.get("FAL_BRAND", "").strip() or "unlabeled"
campaign = os.environ.get("FAL_CAMPAIGN", "").strip() or "unlabeled"
asset = os.environ.get("FAL_ASSET", "").strip() or "unlabeled"
kept = os.environ.get("FAL_KEPT", "").strip() or "pending"
notes = os.environ.get("FAL_NOTES", "").strip()

# price lookup (by exact model id)
cost = ""
try:
    with open(PRICES, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            if row["model"].strip() == model:
                cost = row["est_usd"].strip()
                break
except FileNotFoundError:
    pass
if cost == "":
    notes = (notes + " " if notes else "") + "[cost unknown - add price to infra/fal/prices.csv]"

# next attempt # = 1 + existing rows for the same brand/campaign/asset
attempt = 1
existing = []
if os.path.exists(LEDGER):
    with open(LEDGER, newline="", encoding="utf-8") as f:
        existing = list(csv.DictReader(f))
    same = [r for r in existing
            if r.get("brand") == brand and r.get("campaign") == campaign and r.get("asset") == asset]
    attempt = len(same) + 1

row = {
    "date": datetime.date.today().isoformat(),
    "brand": brand, "campaign": campaign, "asset": asset,
    "attempt": attempt, "model": model, "size": size,
    "cost_usd": cost, "kept": kept, "notes": notes,
}
fields = ["date", "brand", "campaign", "asset", "attempt", "model", "size", "cost_usd", "kept", "notes"]
new_file = not os.path.exists(LEDGER)
with open(LEDGER, "a", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=fields)
    if new_file:
        w.writeheader()
    w.writerow(row)

print(f"logged: {brand}/{campaign}/{asset} attempt {attempt}  {model}  ${cost or '?'}")

# regenerate the readable report so totals stay correct
try:
    subprocess.run([sys.executable, ROLLUP], check=False)
except Exception as e:
    sys.stderr.write(f"_log.py: rollup failed: {e}\n")
