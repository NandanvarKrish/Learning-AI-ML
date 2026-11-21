"""Day 7 solution: Matplotlib from the ground up: line, bar, histogram, annotations and a 2x2 dashboard."""
from pathlib import Path

import matplotlib

matplotlib.use("Agg")  # no window needed: figures are saved as PNG files
import matplotlib.pyplot as plt
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
CLEAN = ROOT / "data" / "clean"
OUT = ROOT / "outputs"
OUT.mkdir(exist_ok=True)

monthly = pd.read_csv(CLEAN / "monthly_revenue.csv", parse_dates=["month_end"])
enriched = pd.read_csv(CLEAN / "orders_enriched.csv")

# ---- 1. Line chart: monthly revenue with the 3-month rolling average -------
fig, ax = plt.subplots(figsize=(9, 4.5))
ax.plot(monthly["month_end"], monthly["revenue"] / 1e6, marker="o", label="Monthly revenue")
ax.plot(monthly["month_end"], monthly["rolling_3m"] / 1e6, linestyle="--", label="3-month average")
ax.set_title("Brightcart monthly net revenue")
ax.set_xlabel("Month")
ax.set_ylabel("Revenue (million)")
ax.legend()
ax.grid(alpha=0.3)
fig.tight_layout()
fig.savefig(OUT / "d07_monthly_revenue.png", dpi=120)
print("CHECK line_points", len(ax.lines[0].get_xdata()))

# ---- 2. Bar chart with labels: revenue by category ---------------------------
by_cat = enriched.groupby("category")["net_revenue"].sum().sort_values(ascending=False) / 1e6
fig, ax = plt.subplots(figsize=(7, 4))
bars = ax.bar(by_cat.index, by_cat.values, color="#2563EB")
ax.bar_label(bars, fmt="%.1fM", padding=3)            # value labels on each bar
ax.set_title("Net revenue by category")
ax.set_ylabel("Revenue (million)")
ax.set_ylim(0, by_cat.max() * 1.15)                   # headroom for the labels
fig.tight_layout()
fig.savefig(OUT / "d07_category_bars.png", dpi=120)
print("CHECK top_bar_height", round(float(bars[0].get_height()), 2))

# ---- 3. Histogram: delivery days with a median line -------------------------
median = enriched["delivery_days"].median()
fig, ax = plt.subplots(figsize=(7, 4))
ax.hist(enriched["delivery_days"], bins=range(1, 27), color="#0891B2", edgecolor="white")
ax.axvline(median, color="red", linestyle="--")
ax.annotate(f"median {median:.0f} days", xy=(median, ax.get_ylim()[1] * 0.9),
            xytext=(median + 3, ax.get_ylim()[1] * 0.9), arrowprops={"arrowstyle": "->"})
ax.set_title("Delivery time distribution")
ax.set_xlabel("Days to deliver")
ax.set_ylabel("Orders")
fig.tight_layout()
fig.savefig(OUT / "d07_delivery_hist.png", dpi=120)
print("CHECK delivery_median", median)

# ---- 4. Dashboard: 2x2 grid of the three charts above, built with subplots ---
fig, axes = plt.subplots(2, 2, figsize=(12, 8))
axes[0, 0].plot(monthly["month_end"], monthly["revenue"] / 1e6, color="#2563EB")
axes[0, 0].set_title("Monthly revenue (M)")
axes[0, 1].bar(by_cat.index, by_cat.values, color="#2563EB")
axes[0, 1].set_title("Revenue by category (M)")
axes[0, 1].tick_params(axis="x", rotation=20)
axes[1, 0].hist(enriched["delivery_days"], bins=range(1, 27), color="#0891B2")
axes[1, 0].set_title("Delivery days")
channel_share = enriched.groupby("channel")["net_revenue"].sum()
axes[1, 1].pie(channel_share.values, labels=channel_share.index, autopct="%1.0f%%")
axes[1, 1].set_title("Channel share")
fig.suptitle("Brightcart dashboard", fontsize=14)
fig.tight_layout()
fig.savefig(OUT / "d07_dashboard.png", dpi=120)
print("CHECK dashboard_axes", len(fig.axes))
print("CHECK channel_top", channel_share.idxmax())
