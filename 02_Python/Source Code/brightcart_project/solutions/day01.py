"""Day 1 solution: set up, NumPy basics, and a first look at the raw Brightcart files."""
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"

# --- NumPy warm-up -----------------------------------------------------------
prices = np.array([1200.0, 850.5, 430.0, 2999.9])
print("CHECK np_mean", round(prices.mean(), 2))
print("CHECK np_max_index", int(prices.argmax()))

grid = np.arange(12).reshape(3, 4)
print("CHECK grid_shape", grid.shape)
print("CHECK grid_col_sums", grid.sum(axis=0).tolist())

# --- Load the three raw files -----------------------------------------------
orders = pd.read_csv(DATA / "orders_raw.csv")
customers = pd.read_csv(DATA / "customers.csv")
products = pd.read_csv(DATA / "products.csv")

print("CHECK orders_shape", orders.shape)
print("CHECK customers_shape", customers.shape)
print("CHECK products_shape", products.shape)

# --- First look: types, missing values, duplicates, labels ------------------
print("CHECK dtype_counts", dict(sorted(orders.dtypes.astype(str).value_counts().items())))
missing = orders.isna().sum()
print("CHECK missing_unit_price", int(missing["unit_price"]))
print("CHECK missing_region", int(missing["region"]))
print("CHECK missing_delivery_days", int(missing["delivery_days"]))
print("CHECK duplicate_rows", int(orders.duplicated().sum()))
print("CHECK channel_values", sorted(orders["channel"].unique()))
print("CHECK returned_values", sorted(orders["returned"].unique()))
print("CHECK date_range", orders["order_date"].min(), orders["order_date"].max())
print("CHECK qty_min", int(orders["qty"].min()))
print("CHECK delivery_max", float(orders["delivery_days"].max()))
print("CHECK product_rows_duplicated", int(products["product_id"].duplicated().sum()))
