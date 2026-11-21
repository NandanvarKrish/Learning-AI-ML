"""Day 6 solution: customer analytics with pandas: RFM scores, value segments and a cohort retention table."""
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
CLEAN = ROOT / "data" / "clean"

df = pd.read_csv(CLEAN / "orders_enriched.csv", parse_dates=["order_date"])
customers = pd.read_csv(CLEAN / "customers_clean.csv")

# The analysis date is the day after the last order, so 'recency' is never zero.
as_of = df["order_date"].max() + pd.Timedelta(days=1)

# ---- RFM: recency, frequency, monetary, one row per customer -----------------
rfm = df.groupby("customer_id").agg(
    last_order=("order_date", "max"),
    frequency=("order_id", "count"),
    monetary=("net_revenue", "sum"),
)
rfm["recency_days"] = (as_of - rfm["last_order"]).dt.days
print("CHECK active_customers", len(rfm))
print("CHECK customers_never_ordered", int((~customers["customer_id"].isin(rfm.index)).sum()))
print("CHECK median_recency", float(rfm["recency_days"].median()))

# Scores 1 to 5 using quintiles. rank(method='first') breaks ties so qcut never fails.
# Lower recency is better, so its labels run the other way.
rfm["R"] = pd.qcut(rfm["recency_days"].rank(method="first"), 5, labels=[5, 4, 3, 2, 1]).astype(int)
rfm["F"] = pd.qcut(rfm["frequency"].rank(method="first"), 5, labels=[1, 2, 3, 4, 5]).astype(int)
rfm["M"] = pd.qcut(rfm["monetary"].rank(method="first"), 5, labels=[1, 2, 3, 4, 5]).astype(int)
rfm["score"] = rfm["R"] + rfm["F"] + rfm["M"]
print("CHECK rfm_score_range", int(rfm["score"].min()), int(rfm["score"].max()))

# Rule-based segments on the total score.
def label(score):
    if score >= 13:
        return "Champions"
    if score >= 10:
        return "Loyal"
    if score >= 7:
        return "At risk"
    return "Lapsed"

rfm["segment"] = rfm["score"].apply(label)
seg = rfm.groupby("segment").agg(customers=("monetary", "size"), avg_value=("monetary", "mean"))
print("CHECK champions_count", int(seg.loc["Champions", "customers"]))
print("CHECK champions_avg_value", round(float(seg.loc["Champions", "avg_value"]), 2))

# Share of revenue from the top 20 percent of customers (a Pareto check).
top_20 = rfm["monetary"].sort_values(ascending=False).head(int(len(rfm) * 0.2)).sum()
print("CHECK top20_revenue_share", round(top_20 / rfm["monetary"].sum() * 100, 2))

# ---- cohort retention: first purchase month vs months since first purchase ----
df["order_month"] = df["order_date"].dt.to_period("M")
first = df.groupby("customer_id")["order_month"].min().rename("cohort")
df = df.join(first, on="customer_id")
df["period_number"] = (df["order_month"] - df["cohort"]).apply(lambda d: d.n)

cohort_counts = df.groupby(["cohort", "period_number"])["customer_id"].nunique().unstack("period_number")
cohort_sizes = cohort_counts[0]
retention = cohort_counts.div(cohort_sizes, axis=0) * 100
print("CHECK cohorts", cohort_counts.shape[0])
print("CHECK cohort_month1_retention_first", round(float(retention.iloc[0, 1]), 2))
print("CHECK retention_month0_all", bool(np.allclose(retention[0].dropna(), 100)))

rfm.to_csv(CLEAN / "rfm.csv")
