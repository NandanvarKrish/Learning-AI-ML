"""Day 5 solution: time series with pandas: monthly resample, growth, rolling averages, channel mix over time."""
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
CLEAN = ROOT / "data" / "clean"

df = pd.read_csv(CLEAN / "orders_enriched.csv", parse_dates=["order_date"])

# A time series needs a DatetimeIndex so resample() and rolling() know the calendar.
ts = df.set_index("order_date").sort_index()

# ---- monthly totals -----------------------------------------------------------
monthly = ts["net_revenue"].resample("ME").sum()          # 'ME' = month end
print("CHECK months", len(monthly))
print("CHECK first_month_revenue", round(monthly.iloc[0], 2))
print("CHECK best_month", monthly.idxmax().strftime("%Y-%m"))
print("CHECK best_month_revenue", round(monthly.max(), 2))

# ---- month-over-month growth and a 3-month rolling average -------------------
mom = monthly.pct_change() * 100
roll3 = monthly.rolling(window=3).mean()
print("CHECK mom_2026_01_pct", round(float(mom.loc["2026-01"].iloc[0]), 2))
print("CHECK roll3_last", round(float(roll3.iloc[-1]), 2))

# ---- Q4 versus the rest of the year -----------------------------------------
q = ts["net_revenue"].resample("QE").sum()                 # quarter end
print("CHECK quarters", len(q))
print("CHECK strongest_quarter", q.idxmax().strftime("%Y-Q") + str((q.idxmax().month - 1) // 3 + 1))

# ---- channel mix over time (share of revenue per month) ----------------------
by_month_channel = ts.groupby([pd.Grouper(freq="ME"), "channel"])["net_revenue"].sum().unstack("channel")
share = by_month_channel.div(by_month_channel.sum(axis=1), axis=0) * 100
print("CHECK app_share_first_month", round(share["App"].iloc[0], 2))
print("CHECK app_share_last_month", round(share["App"].iloc[-1], 2))

# ---- busiest weekday, using the datetime index ------------------------------
weekday = ts["net_revenue"].groupby(ts.index.day_name()).sum().sort_values(ascending=False)
print("CHECK best_weekday", weekday.index[0])

# ---- save the monthly table for Day 7 and Day 8 -----------------------------
out = pd.DataFrame({"revenue": monthly, "mom_pct": mom, "rolling_3m": roll3})
out.index.name = "month_end"
out.to_csv(CLEAN / "monthly_revenue.csv")
