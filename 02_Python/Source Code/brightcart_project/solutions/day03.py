"""Day 3 solution: clean the raw Brightcart data with pandas and write checkpoint files.

Writes data/clean/orders_clean.csv, customers_clean.csv and products_clean.csv.
Days 4 to 10 start from these files.
"""
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
CLEAN = DATA / "clean"
CLEAN.mkdir(parents=True, exist_ok=True)

report = {}  # every cleaning step is counted, so the report can be checked later

# ---- products: remove duplicate product rows --------------------------------
products = pd.read_csv(DATA / "products.csv")
report["product_rows_before"] = len(products)
products = products.drop_duplicates(subset="product_id", keep="first")
report["product_rows_after"] = len(products)

# ---- customers: normalise labels, fill missing city -------------------------
customers = pd.read_csv(DATA / "customers.csv")
customers["segment"] = customers["segment"].str.strip().str.title()     # 'consumer' -> 'Consumer'
customers["city"] = customers["city"].fillna("Unknown")
customers["signup_date"] = pd.to_datetime(customers["signup_date"])
report["segments"] = customers["segment"].value_counts().to_dict()

# ---- orders: step by step ---------------------------------------------------
orders = pd.read_csv(DATA / "orders_raw.csv")
report["orders_raw"] = len(orders)

# 1. Exact duplicate rows (the export repeated some orders).
orders = orders.drop_duplicates()
report["after_remove_duplicates"] = len(orders)

# 2. Normalise labels so 'web' and 'Web' are one category.
orders["channel"] = orders["channel"].str.strip().str.title()
orders["returned_flag"] = orders["returned"].str.strip().str.lower().isin(["yes", "y"]).astype(int)
orders = orders.drop(columns="returned")

# 3. Orders for customers we do not know are unusable for customer analysis.
known = orders["customer_id"].isin(customers["customer_id"])
report["orphan_customer_rows_dropped"] = int((~known).sum())
orders = orders[known]

# 4. Quantity must be at least 1.
bad_qty = orders["qty"] < 1
report["zero_qty_rows_dropped"] = int(bad_qty.sum())
orders = orders[~bad_qty]

# 5. Missing unit price: use the product's list price (a lookup join).
orders = orders.merge(products[["product_id", "list_price"]], on="product_id", how="left")
report["unit_price_filled_from_list"] = int(orders["unit_price"].isna().sum())
orders["unit_price"] = orders["unit_price"].fillna(orders["list_price"])
orders = orders.drop(columns="list_price")

# 6. Delivery days: above 60 is an error, and missing values get the median.
outlier = orders["delivery_days"] > 60
report["delivery_outliers_set_missing"] = int(outlier.sum())
orders.loc[outlier, "delivery_days"] = float("nan")
median_delivery = orders["delivery_days"].median()
report["delivery_median_used"] = float(median_delivery)
orders["delivery_days"] = orders["delivery_days"].fillna(median_delivery)

# 7. Missing region becomes an explicit 'Unknown' rather than a hole.
report["region_unknown_filled"] = int(orders["region"].isna().sum())
orders["region"] = orders["region"].fillna("Unknown")

# 8. Dates: text to real datetimes.
orders["order_date"] = pd.to_datetime(orders["order_date"])

report["orders_clean"] = len(orders)

# ---- write checkpoints ------------------------------------------------------
orders.to_csv(CLEAN / "orders_clean.csv", index=False)
customers.to_csv(CLEAN / "customers_clean.csv", index=False)
products.to_csv(CLEAN / "products_clean.csv", index=False)

for key, value in report.items():
    print("CHECK", key, value)
print("CHECK clean_nulls_total", int(orders.isna().sum().sum()))
print("CHECK clean_channel_values", sorted(orders["channel"].unique()))
print("CHECK clean_returned_rate", round(float(orders["returned_flag"].mean()), 4))
