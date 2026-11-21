"""Day 2 solution: vectorised NumPy for revenue, NaN handling, boolean masks and broadcasting."""
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"

orders = pd.read_csv(DATA / "orders_raw.csv")

# Pull the columns out as NumPy arrays (no Python loops anywhere below).
qty = orders["qty"].to_numpy(dtype=float)
price = orders["unit_price"].to_numpy(dtype=float)          # contains NaN where price is missing
disc = orders["discount_pct"].to_numpy(dtype=float)
delivery = orders["delivery_days"].to_numpy(dtype=float)     # contains NaN and outliers

# NaN-aware statistics: a plain mean would be NaN if any value is missing.
print("CHECK price_mean_with_nan", np.isnan(np.mean(price)))
print("CHECK price_mean_ignoring_nan", round(float(np.nanmean(price)), 2))
print("CHECK missing_price_count", int(np.isnan(price).sum()))

# Vectorised revenue: quantity * price * (1 - discount).  Broadcasting does the work.
valid = (qty > 0) & ~np.isnan(price)                         # boolean mask: usable rows
revenue = np.where(valid, qty * price * (1 - disc / 100), 0.0)
print("CHECK usable_rows", int(valid.sum()))
print("CHECK total_revenue", round(float(revenue.sum()), 2))

# Broadcasting: a discount rate applied to a whole row of values at once.
rate = np.array([0.05, 0.10, 0.20])                          # shape (3,)
amounts = np.array([[1000.0], [2000.0]])                     # shape (2, 1)
print("CHECK broadcast_shape", (amounts * (1 - rate)).shape)
print("CHECK broadcast_first_row", np.round(amounts[0] * (1 - rate), 2).tolist())

# Outlier mask on delivery days: anything above 60 is impossible for this business.
outlier = delivery > 60
print("CHECK delivery_outliers", int(np.nansum(outlier)))
clean_delivery = np.where(outlier | np.isnan(delivery), np.nan, delivery)
print("CHECK delivery_median_clean", round(float(np.nanmedian(clean_delivery)), 2))

# Aggregation along an axis: revenue per discount level, using a 2-D table.
levels = np.array([0, 5, 10, 15, 20, 25, 30], dtype=float)
rev_by_level = np.array([revenue[disc == lv].sum() for lv in levels])  # small loop over 7 levels is fine
print("CHECK revenue_top_level", float(levels[rev_by_level.argmax()]))
share = rev_by_level / rev_by_level.sum()
print("CHECK share_no_discount", round(float(share[0]), 4))
