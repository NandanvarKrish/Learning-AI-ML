"""Day 10 capstone: one script that runs the whole Brightcart pipeline and writes the report.

Run from the project folder:   python solutions/day10.py
It runs the Day 3 cleaning, Day 4 features, Day 5 monthly series, Day 6 customers and
Day 9 tests, then writes outputs/kpis.csv, outputs/charts/ and outputs/executive_summary.md.
"""
import subprocess
import sys
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
SOL = ROOT / "solutions"
OUT = ROOT / "outputs"
(OUT / "charts").mkdir(parents=True, exist_ok=True)

# 1. Run the pipeline stages in order. A stage that fails stops the build.
for stage in ["day03.py", "day04.py", "day05.py", "day06.py", "day07.py", "day08.py", "day09.py"]:
    result = subprocess.run([sys.executable, str(SOL / stage)], capture_output=True, text=True, cwd=ROOT)
    if result.returncode != 0:
        print(f"STAGE FAILED {stage}\n{result.stderr}")
        sys.exit(1)
print("CHECK stages_ok", 7)

# 2. Load the checkpoints the stages produced.
CLEAN = ROOT / "data" / "clean"
df = pd.read_csv(CLEAN / "orders_enriched.csv", parse_dates=["order_date"])
monthly = pd.read_csv(CLEAN / "monthly_revenue.csv", parse_dates=["month_end"])
rfm = pd.read_csv(CLEAN / "rfm.csv")

# 3. KPI table: one row per headline number, so the report can be checked by anyone.
last_12 = df[df["order_date"] > df["order_date"].max() - pd.DateOffset(months=12)]
prev_12 = df[(df["order_date"] <= df["order_date"].max() - pd.DateOffset(months=12))
             & (df["order_date"] > df["order_date"].max() - pd.DateOffset(months=24))]
kpis = pd.DataFrame([
    ("Net revenue, last 12 months", last_12["net_revenue"].sum()),
    ("Net revenue, previous 12 months", prev_12["net_revenue"].sum()),
    ("Orders, last 12 months", len(last_12)),
    ("Gross margin %, all orders", df["margin"].sum() / df["net_revenue"].sum() * 100),
    ("Return rate %, all orders", df["returned_flag"].mean() * 100),
    ("Average delivery days", df["delivery_days"].mean()),
    ("Active customers", df["customer_id"].nunique()),
    ("Champion customers (RFM)", int((rfm["segment"] == "Champions").sum())),
], columns=["kpi", "value"])
kpis["value"] = kpis["value"].round(2)
kpis.to_csv(OUT / "kpis.csv", index=False)
growth = (kpis.loc[0, "value"] / kpis.loc[1, "value"] - 1) * 100
print("CHECK kpi_rows", len(kpis))
print("CHECK revenue_growth_pct", round(growth, 2))

# 4. Copy the charts from the chart day into outputs/charts.
for png in (ROOT / "outputs").glob("d0*.png"):
    (OUT / "charts" / png.name).write_bytes(png.read_bytes())

# 5. Executive summary: numbers come from the calculations above, not typed by hand.
best_month = monthly.loc[monthly["revenue"].idxmax(), "month_end"].strftime("%B %Y")
summary = f"""# Brightcart analysis: executive summary

## Headline numbers
- Net revenue in the last 12 months: {kpis.loc[0, 'value']:,.0f}
- Net revenue in the previous 12 months: {kpis.loc[1, 'value']:,.0f}
- Year-on-year change: {growth:+.1f} percent
- Gross margin: {kpis.loc[3, 'value']:.1f} percent
- Return rate: {kpis.loc[4, 'value']:.1f} percent of orders

## What the data says
- Best month for revenue: {best_month}.
- Electronics is the largest category and has the highest return rate.
- Discounts of 15 percent or more do not produce a statistically significant change in returns (permutation test, see Day 9).
- Average delivery is about {kpis.loc[5, 'value']:.1f} days, with a few very late deliveries removed as errors.

## Data quality
- Duplicate rows, orphan customers, zero quantities and missing values were removed or filled. See the Day 3 cleaning report.

## Method
Python 3 with NumPy, pandas, Matplotlib and Seaborn. All numbers come from solutions/day03.py to day09.py.
"""
(OUT / "executive_summary.md").write_text(summary)
print("CHECK summary_lines", len(summary.splitlines()))
