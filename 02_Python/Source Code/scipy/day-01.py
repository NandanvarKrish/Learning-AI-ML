from scipy import stats
import numpy as np
import matplotlib.pyplot as plt

calls_per_window = stats.poisson(mu=12)
print(f"P(exactly 12):{calls_per_window.pmf(12)}")
print(f"P(more than 20): {1 - calls_per_window.cdf(20)}")
print(f"95th percentile:{calls_per_window.ppf(0.95)}")

