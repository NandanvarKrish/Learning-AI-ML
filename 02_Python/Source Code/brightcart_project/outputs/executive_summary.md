# Brightcart analysis: executive summary

## Headline numbers
- Net revenue in the last 12 months: 31,532,109
- Net revenue in the previous 12 months: 25,950,565
- Year-on-year change: +21.5 percent
- Gross margin: 40.4 percent
- Return rate: 6.9 percent of orders

## What the data says
- Best month for revenue: September 2026.
- Electronics is the largest category and has the highest return rate.
- Discounts of 15 percent or more do not produce a statistically significant change in returns (permutation test, see Day 9).
- Average delivery is about 4.8 days, with a few very late deliveries removed as errors.

## Data quality
- Duplicate rows, orphan customers, zero quantities and missing values were removed or filled. See the Day 3 cleaning report.

## Method
Python 3 with NumPy, pandas, Matplotlib and Seaborn. All numbers come from solutions/day03.py to day09.py.
