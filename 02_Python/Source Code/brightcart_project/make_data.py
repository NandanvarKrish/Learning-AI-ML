"""Generate the Brightcart raw data (synthetic, reproducible).

Run:  python make_data.py
Writes data/customers.csv, data/products.csv and data/orders_raw.csv.
The data is deliberately messy (missing values, duplicates, inconsistent labels,
impossible values) so that Day 3 cleaning has real work to do.
"""
from pathlib import Path

import numpy as np
import pandas as pd

rng = np.random.default_rng(2026)
DATA = Path(__file__).resolve().parent / "data"
DATA.mkdir(exist_ok=True)

# ---- customers -------------------------------------------------------------
n_cust = 800
cust_ids = [f"C{i:04d}" for i in range(1, n_cust + 1)]
signup = pd.to_datetime("2024-01-01") + pd.to_timedelta(rng.integers(0, 900, n_cust), unit="D")
segment = rng.choice(["Consumer", "Small Business", "Enterprise"], n_cust, p=[0.7, 0.22, 0.08])
city = rng.choice(["Mumbai", "Delhi", "Bengaluru", "Pune", "Chennai", "Hyderabad"], n_cust)
customers = pd.DataFrame({"customer_id": cust_ids, "signup_date": signup.strftime("%Y-%m-%d"),
                          "segment": segment, "city": city})
# messy labels and missing cities
seg_mess = rng.random(n_cust) < 0.06
customers.loc[seg_mess, "segment"] = customers.loc[seg_mess, "segment"].str.lower()
customers.loc[rng.random(n_cust) < 0.03, "city"] = np.nan
customers.to_csv(DATA / "customers.csv", index=False)

# ---- products --------------------------------------------------------------
n_prod = 60
cats = ["Electronics", "Home", "Apparel", "Books", "Sports"]
prod_cat = rng.choice(cats, n_prod, p=[0.25, 0.2, 0.25, 0.1, 0.2])
base_price = {"Electronics": 9000, "Home": 2500, "Apparel": 1500, "Books": 600, "Sports": 3000}
unit_price_list = np.array([base_price[c] for c in prod_cat]) * rng.uniform(0.6, 1.6, n_prod)
products = pd.DataFrame({
    "product_id": [f"P{i:03d}" for i in range(1, n_prod + 1)],
    "category": prod_cat,
    "brand": rng.choice(["Aurora", "Bolt", "Cedar", "Dune", "Evo"], n_prod),
    "list_price": np.round(unit_price_list, 2),
    "unit_cost": np.round(unit_price_list * rng.uniform(0.45, 0.7, n_prod), 2),
})
products = pd.concat([products, products.iloc[[3, 17]]], ignore_index=True)  # 2 duplicate rows
products.to_csv(DATA / "products.csv", index=False)

# ---- orders ----------------------------------------------------------------
n = 9000
start = pd.Timestamp("2025-01-01")
days_span = (pd.Timestamp("2026-10-31") - start).days
# more orders later in the year (Q4 peak) and a growing app channel
day_offsets = np.sort(rng.integers(0, days_span + 1, n))
order_date = start + pd.to_timedelta(day_offsets, unit="D")
cust_pick = rng.integers(1, n_cust + 1, n)
prod_pick = rng.integers(1, n_prod + 1, n)
channel = rng.choice(["Web", "App", "Store", "Marketplace"], n, p=[0.35, 0.3, 0.15, 0.2])
region = rng.choice(["North", "South", "East", "West"], n)
qty = rng.choice([1, 2, 3, 4, 5], n, p=[0.6, 0.2, 0.1, 0.06, 0.04])
discount = rng.choice([0, 5, 10, 15, 20, 25, 30], n, p=[0.45, 0.15, 0.15, 0.12, 0.07, 0.04, 0.02]).astype(float)
ret_prob = np.where(prod_cat[prod_pick - 1] == "Electronics", 0.12, 0.05)
returned = rng.random(n) < ret_prob
delivery = np.clip(rng.gamma(3.0, 1.6, n).round(), 1, 25)

orders = pd.DataFrame({
    "order_id": [f"O{i:05d}" for i in range(1, n + 1)],
    "order_date": pd.DatetimeIndex(order_date).strftime("%Y-%m-%d"),
    "customer_id": [f"C{c:04d}" for c in cust_pick],
    "product_id": [f"P{p:03d}" for p in prod_pick],
    "channel": channel,
    "region": region,
    "qty": qty,
    "discount_pct": discount,
    "returned": np.where(returned, "yes", "no"),
    "delivery_days": delivery,
})
# list price is looked up from products at generation time (for realism); some rows have it missing
price_lookup = dict(zip(products["product_id"], products["list_price"]))
orders["unit_price"] = np.round(orders["product_id"].map(price_lookup).astype(float)
                                * rng.uniform(0.97, 1.03, n), 2)

# messy values
idx = rng.choice(n, 180, replace=False)
orders.loc[idx[:60], "unit_price"] = np.nan                  # missing price
orders.loc[idx[60:90], "delivery_days"] = np.nan             # missing delivery time
orders.loc[idx[90:110], "customer_id"] = "C9999"             # orphan customer (not in customers.csv)
orders.loc[idx[110:130], "qty"] = 0                          # impossible quantity
orders.loc[idx[130:150], "channel"] = orders.loc[idx[130:150], "channel"].str.lower()
orders.loc[idx[150:165], "delivery_days"] = 300.0            # outliers
orders.loc[idx[165:180], "returned"] = "Y"                   # alternative label for yes
orders.loc[rng.choice(n, 40, replace=False), "region"] = None  # missing region
dupes = orders.sample(60, random_state=7)                    # exact duplicate rows
orders = pd.concat([orders, dupes], ignore_index=True)
orders = orders.sample(frac=1, random_state=11).reset_index(drop=True)  # shuffle, like a real export
orders.to_csv(DATA / "orders_raw.csv", index=False)

print("customers", customers.shape, "products", products.shape, "orders_raw", orders.shape)
