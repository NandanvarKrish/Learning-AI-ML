"""Day 9 solution: return analysis and hypothesis testing with NumPy and pandas.

Question: do bigger discounts (15 percent or more) lead to more returns?
Method: observed difference in return rate, a permutation test, and a bootstrap confidence interval.
"""
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
CLEAN = ROOT / "data" / "clean"

df = pd.read_csv(CLEAN / "orders_enriched.csv")
rng = np.random.default_rng(42)  # fixed seed: the same numbers every run

# ---- descriptive: return rate by category and by channel ---------------------
print("CHECK overall_return_rate", round(df["returned_flag"].mean() * 100, 2))
by_cat = df.groupby("category")["returned_flag"].mean().mul(100).round(2).sort_values(ascending=False)
print("CHECK highest_return_category", by_cat.index[0], by_cat.iloc[0])
by_channel = df.groupby("channel")["returned_flag"].mean().mul(100).round(2)
print("CHECK lowest_return_channel", by_channel.idxmin(), by_channel.min())

# ---- the question: discount group comparison --------------------------------
big = df["discount_pct"] >= 15
rate_big = df.loc[big, "returned_flag"].mean()
rate_small = df.loc[~big, "returned_flag"].mean()
observed = rate_big - rate_small
print("CHECK big_discount_orders", int(big.sum()))
print("CHECK rate_difference_pts", round(observed * 100, 3))

# ---- permutation test: shuffle the discount labels and see how big a gap appears by chance
flags = df["returned_flag"].to_numpy()
is_big = big.to_numpy()
n_perm = 5000
diffs = np.empty(n_perm)
for i in range(n_perm):
    shuffled = rng.permutation(is_big)
    diffs[i] = flags[shuffled].mean() - flags[~shuffled].mean()
p_value = np.mean(np.abs(diffs) >= abs(observed))
print("CHECK permutation_p_value", round(float(p_value), 3))
print("CHECK significant_at_5pct", bool(p_value < 0.05))

# ---- bootstrap: a 95 percent confidence interval for the average delivery time ---
delivery = df["delivery_days"].to_numpy()
boot_means = np.array([rng.choice(delivery, size=len(delivery), replace=True).mean() for _ in range(2000)])
low, high = np.percentile(boot_means, [2.5, 97.5])
print("CHECK delivery_mean", round(float(delivery.mean()), 3))
print("CHECK delivery_ci_low", round(float(low), 3))
print("CHECK delivery_ci_high", round(float(high), 3))

# ---- correlation: does longer delivery relate to returns? ---------------------
r = np.corrcoef(delivery, flags)[0, 1]
print("CHECK corr_delivery_return", round(float(r), 4))

# ---- a small summary table for the report --------------------------------------
summary = pd.DataFrame({
    "return_rate_pct": [rate_small * 100, rate_big * 100],
    "orders": [int((~big).sum()), int(big.sum())],
}, index=["discount under 15", "discount 15 or more"])
summary.to_csv(CLEAN / "discount_return_summary.csv")
print("CHECK summary_rows", len(summary))
