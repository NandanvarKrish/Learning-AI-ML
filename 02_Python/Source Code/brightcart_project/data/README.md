# Brightcart data dictionary

Brightcart is a fictional online retailer. **All data is synthetic**: it was generated
to look like real business data, with realistic mess (duplicates, blank cells,
inconsistent spelling, impossible values). Do not treat any number as a real business fact.

## Raw files (do not edit)

### customers.csv (800 rows)
| column | meaning |
|---|---|
| customer_id | Unique customer code, such as C0001 |
| signup_date | Date the customer joined (YYYY-MM-DD) |
| segment | Consumer, Small Business or Enterprise |
| city | Home city |

### products.csv (62 rows, 2 duplicated)
| column | meaning |
|---|---|
| product_id | Product code, such as P001 |
| category | Electronics, Home, Books, Apparel, Sports or similar |
| brand | Brand name |
| list_price | Standard selling price (the data does not state a currency) |
| unit_cost | Cost to Brightcart per unit |

### orders_raw.csv (9,060 rows)
| column | meaning | known problems |
|---|---|---|
| order_id | Order code, such as O05018 | 60 exact duplicate rows |
| order_date | Date of the order | range 2025-01-01 to 2026-10-31 |
| customer_id | Who ordered | 20 IDs not in customers.csv |
| product_id | What was ordered | none |
| channel | Web, App, Store or Marketplace | mixed case, such as "web" or "APP" |
| region | Sales region | 42 blank |
| qty | Units ordered | 20 rows with qty 0 |
| discount_pct | Discount in percent | none |
| returned | Whether the order came back | yes, no, Y and other spellings |
| delivery_days | Days to deliver | 30 blank; a few values as high as 300 |
| unit_price | Price charged per unit | 60 blank |

## Clean files (produced by solutions/day03.py to day09.py)

### data/clean/orders_clean.csv (8,960 rows)
Raw orders after cleaning: duplicates removed, channel standardised, returned turned
into returned_flag (1 = returned, 0 = not), orphan and zero-quantity rows removed,
blank unit_price filled from list_price, delivery outliers (more than 60 days) set to
the median (4 days), blank region set to "Unknown".

### data/clean/orders_enriched.csv (8,960 rows)
orders_clean joined with product and customer details, plus:
| column | meaning |
|---|---|
| gross_revenue | qty x unit_price |
| net_revenue | gross_revenue after the discount |
| cost | qty x unit_cost |
| margin, margin_pct | net_revenue minus cost, and as a percent of net_revenue |

### data/clean/customers_clean.csv, products_clean.csv
Cleaned copies of the customer and product tables.

### data/clean/monthly_revenue.csv (22 rows)
| column | meaning |
|---|---|
| month_end | Last day of the month |
| revenue | Total net revenue in the month |
| mom_pct | Change from the previous month, in percent |
| rolling_3m | Average of the last three months |

### data/clean/rfm.csv (800 rows)
| column | meaning |
|---|---|
| last_order, frequency, monetary | Last order date, number of orders, total net revenue |
| recency_days | Days since the last order, at the data end date |
| R, F, M | Scores from 1 to 5 for recency, frequency and monetary value |
| score | R + F + M (range 3 to 15) |
| segment | Champions, Loyal, At risk or Lapsed |

### data/clean/discount_return_summary.csv
Return rate and order count for orders with a discount under 15 percent and 15 percent or more.

## Output files (produced by solutions/day10.py)
- outputs/kpis.csv: the eight headline numbers used in the executive summary.
- outputs/executive_summary.md: the written summary.
- outputs/charts/: the chart images.
