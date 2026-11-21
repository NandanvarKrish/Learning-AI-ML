"""Day 4 solution: joins, features (revenue, cost, margin), groupby, pivot tables and named aggregation."""
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
CLEAN = ROOT / "data" / "clean"

orders = pd.read_csv(CLEAN / "orders_clean.csv", parse_dates=["order_date"])
customers = pd.read_csv(CLEAN / "customers_clean.csv")
products = pd.read_csv(CLEAN / "products_clean.csv")

# ---- joins -------------------------------------------------------------------
# Left join keeps every order even if a product or customer is missing from the lookup table.
df = orders.merge(products[["product_id", "category", "brand", "unit_cost"]], on="product_id", how="left")
df = df.merge(customers[["customer_id", "segment", "city"]], on="customer_id", how="left")
print("CHECK rows_after_join", len(df))
print("CHECK missing_category_after_join", int(df["category"].isna().sum()))
print("CHECK missing_segment_after_join", int(df["segment"].isna().sum()))

# ---- features ----------------------------------------------------------------
df["gross_revenue"] = df["qty"] * df["unit_price"]
df["net_revenue"] = df["gross_revenue"] * (1 - df["discount_pct"] / 100)
df["cost"] = df["qty"] * df["unit_cost"]
df["margin"] = df["net_revenue"] - df["cost"]
df["margin_pct"] = df["margin"] / df["net_revenue"] * 100

print("CHECK total_net_revenue", round(df["net_revenue"].sum(), 2))
print("CHECK overall_margin_pct", round(df["margin"].sum() / df["net_revenue"].sum() * 100, 2))

# ---- groupby: one row per category -----------------------------------------
by_cat = df.groupby("category").agg(
    orders=("order_id", "count"),
    revenue=("net_revenue", "sum"),
    avg_order_value=("net_revenue", "mean"),
    margin_pct=("margin_pct", "mean"),
).sort_values("revenue", ascending=False)
print("CHECK top_category", by_cat.index[0])
print("CHECK top_category_revenue", round(by_cat["revenue"].iloc[0], 2))

# ---- named aggregation with a multi-column groupby ------------------------
by_seg_channel = df.groupby(["segment", "channel"])["net_revenue"].sum().unstack("channel")
print("CHECK segment_channel_shape", by_seg_channel.shape)

# ---- pivot_table: region x channel, mean order value -----------------------
pivot = df.pivot_table(index="region", columns="channel", values="net_revenue", aggfunc="mean")
print("CHECK pivot_shape", pivot.shape)
print("CHECK pivot_max_cell", round(float(pivot.max().max()), 2))

# ---- segment summary and returns --------------------------------------------
seg = df.groupby("segment").agg(
    customers_orders=("order_id", "count"),
    return_rate=("returned_flag", "mean"),
    avg_qty=("qty", "mean"),
)
print("CHECK enterprise_avg_qty", round(seg.loc["Enterprise", "avg_qty"], 3))
print("CHECK highest_return_segment", seg["return_rate"].idxmax())

# ---- category x discount: does a bigger discount sell more units? -----------
disc_table = df.groupby("discount_pct")["qty"].mean().round(3)
print("CHECK avg_qty_discount_0", disc_table.loc[0])
print("CHECK avg_qty_discount_30", disc_table.loc[30])

df.to_csv(CLEAN / "orders_enriched.csv", index=False)
