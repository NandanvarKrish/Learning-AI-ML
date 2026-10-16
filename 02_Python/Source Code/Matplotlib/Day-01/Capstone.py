import numpy as np
from report import generate_dashboard

# Seed for reproducible business distributions
np.random.seed(10)

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
revenue_2023 = np.random.uniform(40, 70, 12).round(1)
revenue_2024 = (revenue_2023 * np.random.uniform(1.05, 1.25, 12)).round(1)

depts = ['Electronics', 'Apparel', 'Grocery', 'Home', 'Sports']
dept_revenue = np.random.uniform(80, 400, 5).round(1)

customer_spend = np.random.gamma(3, 80, 1000)

ad_spend = np.random.uniform(5, 50, 40)
sales_gen = ad_spend * 8 + np.random.normal(0, 30, 40) + 50

generate_dashboard(
    months=months,
    rev_23=revenue_2023,
    rev_24=revenue_2024,
    depts=depts,
    dept_rev=dept_revenue,
    spend=customer_spend,
    ad_spend=ad_spend,
    sales_gen=sales_gen
)