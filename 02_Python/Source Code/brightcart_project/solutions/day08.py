"""Day 8 solution: Seaborn statistical plots: distributions, categories, heatmap, regression and facets."""
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

ROOT = Path(__file__).resolve().parents[1]
CLEAN = ROOT / "data" / "clean"
OUT = ROOT / "outputs"
OUT.mkdir(exist_ok=True)

df = pd.read_csv(CLEAN / "orders_enriched.csv", parse_dates=["order_date"])
sns.set_theme(style="whitegrid", palette="deep")

# ---- 1. Distribution: order value by segment (histogram with KDE) -----------
g = sns.displot(data=df, x="net_revenue", hue="segment", kind="hist", bins=40,
                multiple="stack", height=4, aspect=1.6)
g.set(title="Order value by segment", xlabel="Net revenue per order", ylabel="Orders")
g.savefig(OUT / "d08_order_value_hist.png", dpi=120)
print("CHECK displot_facets", len(g.axes.flat))

# ---- 2. Categorical comparison: boxplot of order value by category ----------
fig, ax = plt.subplots(figsize=(8, 4.5))
sns.boxplot(data=df, x="category", y="net_revenue", hue="category", legend=False, ax=ax, showfliers=False)
ax.set_title("Order value spread by category (outliers hidden)")
fig.tight_layout()
fig.savefig(OUT / "d08_category_box.png", dpi=120)
medians = df.groupby("category")["net_revenue"].median().round(2)
print("CHECK category_median_max", medians.idxmax())

# ---- 3. Heatmap: revenue by region (rows) and month (columns) ----------------
df["month"] = df["order_date"].dt.month
pivot = df.pivot_table(index="region", columns="month", values="net_revenue", aggfunc="sum") / 1e6
fig, ax = plt.subplots(figsize=(9, 3.8))
sns.heatmap(pivot, cmap="Blues", annot=True, fmt=".1f", cbar_kws={"label": "Revenue (M)"}, ax=ax)
ax.set_title("Revenue by region and calendar month (all years, millions)")
fig.tight_layout()
fig.savefig(OUT / "d08_region_month_heatmap.png", dpi=120)
print("CHECK heatmap_shape", pivot.shape)

# ---- 4. Relationship: quantity vs net revenue with a regression line ---------
fig, ax = plt.subplots(figsize=(7, 4.5))
sns.regplot(data=df.sample(1500, random_state=1), x="qty", y="net_revenue",
            scatter_kws={"alpha": 0.3}, line_kws={"color": "crimson"}, ax=ax)
ax.set_title("Quantity and net revenue (sample of 1,500 orders)")
fig.tight_layout()
fig.savefig(OUT / "d08_qty_revenue_reg.png", dpi=120)
slope = float(pd.Series(df["net_revenue"]).corr(df["qty"]))
print("CHECK qty_revenue_corr", round(slope, 3))

# ---- 5. Faceted bars: average order value by channel, one panel per segment --
bar = sns.catplot(data=df, x="channel", y="net_revenue", col="segment", kind="bar",
                  estimator="mean", errorbar=("ci", 95), height=3.6, aspect=0.9, color="#2563EB")
bar.set_axis_labels("Channel", "Average net revenue")
bar.savefig(OUT / "d08_channel_by_segment.png", dpi=120)
seg_means = df.groupby("segment")["net_revenue"].mean().round(2)
print("CHECK enterprise_avg_order", seg_means["Enterprise"])
print("CHECK facet_count", len(bar.axes.flat))
