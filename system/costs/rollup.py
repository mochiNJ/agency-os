#!/usr/bin/env python3
"""Read generation-ledger.csv + subscriptions.csv and (re)write SPEND-REPORT.md.

Usage (from anywhere):  python system/costs/rollup.py
It never changes the CSVs. It only regenerates the human-readable report so the
totals are always correct. Add a generation = append ONE line to
generation-ledger.csv, then run this. Stdlib only (no installs).
"""
import csv, os, datetime
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
GEN = os.path.join(HERE, "generation-ledger.csv")
SUB = os.path.join(HERE, "subscriptions.csv")
OUT = os.path.join(HERE, "SPEND-REPORT.md")


def money(x):
    return f"${x:,.3f}"


def read_csv(path):
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def num(s):
    try:
        return float(str(s).strip() or 0)
    except ValueError:
        return 0.0


def main():
    gens = read_csv(GEN)
    subs = read_csv(SUB)

    total = sum(num(g["cost_usd"]) for g in gens)

    by_brand = defaultdict(float)
    by_month = defaultdict(float)
    # asset key = (brand, campaign, asset) -> list of gen rows
    by_asset = defaultdict(list)
    for g in gens:
        by_brand[g["brand"]] += num(g["cost_usd"])
        by_month[(g["date"] or "")[:7]] += num(g["cost_usd"])
        by_asset[(g["brand"], g["campaign"], g["asset"])].append(g)

    lines = []
    lines.append("# 💸 Spend Report — AI Agency")
    lines.append("")
    lines.append("> **AUTO-GENERATED — do not edit by hand.** Edit `generation-ledger.csv` or")
    lines.append("> `subscriptions.csv`, then run `python system/costs/rollup.py` to regenerate this.")
    lines.append(f">")
    lines.append(f"> Last generated: {datetime.date.today().isoformat()}")
    lines.append("")
    lines.append(f"**Total generation spend to date: {money(total)}**  ")
    lines.append(f"*(across {len(gens)} generation(s))*")
    lines.append("")

    # --- Per brand ---
    lines.append("## Spend by brand")
    lines.append("")
    lines.append("| Brand | Generation spend |")
    lines.append("|---|---|")
    for b in sorted(by_brand, key=lambda k: -by_brand[k]):
        lines.append(f"| {b} | {money(by_brand[b])} |")
    lines.append(f"| **TOTAL** | **{money(total)}** |")
    lines.append("")

    # --- Per month ---
    lines.append("## Spend by month")
    lines.append("")
    lines.append("| Month | Generation spend |")
    lines.append("|---|---|")
    for m in sorted(by_month):
        lines.append(f"| {m or '(no date)'} | {money(by_month[m])} |")
    lines.append("")

    # --- Per asset (grouped attempts) ---
    lines.append("## Spend by asset (attempts grouped)")
    lines.append("")
    lines.append("Each asset shows every generation attempt + a subtotal, so you can see e.g.")
    lines.append("\"Slide 1 = 2 generations = $X\". `kept` marks which attempt we shipped.")
    lines.append("")
    for (brand, campaign, asset) in sorted(by_asset):
        rows = by_asset[(brand, campaign, asset)]
        sub = sum(num(r["cost_usd"]) for r in rows)
        lines.append(f"### {brand} / {campaign} / **{asset}** — {len(rows)} generation(s), subtotal {money(sub)}")
        lines.append("")
        lines.append("| # | Model | Size | Cost | Kept | Notes |")
        lines.append("|---|---|---|---|---|---|")
        for r in sorted(rows, key=lambda r: num(r["attempt"])):
            lines.append(
                f"| {r['attempt']} | {r['model']} | {r['size']} | {money(num(r['cost_usd']))} "
                f"| {r['kept']} | {r['notes']} |"
            )
        lines.append("")

    # --- Subscriptions ---
    monthly = 0.0
    yearly_as_monthly = 0.0
    lines.append("## Subscriptions & recurring costs")
    lines.append("")
    lines.append("| Service | What | Billing | Amount | Cycle | Status | Notes |")
    lines.append("|---|---|---|---|---|---|---|")
    for s in subs:
        amt = num(s["amount_usd"])
        cyc = (s["cycle"] or "").lower()
        if cyc == "monthly":
            monthly += amt
        elif cyc in ("yearly", "annual"):
            yearly_as_monthly += amt / 12.0
        lines.append(
            f"| {s['service']} | {s['what_it_is']} | {s['billing']} | "
            f"{money(amt) if amt else '-'} | {s['cycle']} | {s['status']} | {s['notes']} |"
        )
    lines.append("")
    est_monthly = monthly + yearly_as_monthly
    lines.append(f"**Fixed recurring ≈ {money(est_monthly)} / month** "
                 f"(monthly subs {money(monthly)} + yearly-as-monthly {money(yearly_as_monthly)}).  ")
    lines.append("*Pay-as-you-go items (fal.ai, Meta Ads) are usage-based, not fixed — see the generation log above for fal usage.*  ")
    lines.append("*Rows marked `CONFIRM` still need real numbers from the user.*")
    lines.append("")

    with open(OUT, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"wrote {OUT}")
    print(f"total generation spend = {money(total)}; fixed recurring ~= {money(est_monthly)}/mo")


if __name__ == "__main__":
    main()
