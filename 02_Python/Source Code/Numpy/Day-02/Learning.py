import numpy as np

# a = np.array([4, 9, 16, 25, 36])
# b = np.array([2, 3,  4,  5,  6])

# print(np.add(a, b))
# print(np.subtract(a, b))
# print(np.multiply(a, b))
# print(np.divide(a, b))
# print(np.power(a, b))
# print(np.mod(a, 3)) 
# print(np.floor_divide(a, b))
# print(np.absolute(np.array([-3, -1, 0, 2, -5])))

# x = np.array([1, 2, 4, 8, 16], dtype=float)

# print(np.exp(x))
# print(np.exp2(x))
# print(np.log(x))
# print(np.log2(x))
# print(np.log10(x))

# principal = 10_000
# rate = 0.08
# years = np.arange(1,11)
# amount = principal * np.exp(rate * years)
# print(np.round(amount, 2))

# angles_deg = np.array([0, 30, 45, 60, 90, 180])

# angles_rad = np.deg2rad(angles_deg)

# print(np.sin(angles_rad))
# print(np.cos(angles_rad))
# print(np.tan(angles_rad))

# print(np.rad2deg(np.arcsin(0.5)))
# print(np.rad2deg(np.arccos(0.5)))
# print(np.rad2deg(np.arctan(1.0)))

# vals = np.array([2.1, 2.5, 2.9, -1.4, -1.6, 3.75])

# print(np.round(vals, 1))  
# print(np.floor(vals))      
# print(np.ceil(vals))       
# print(np.trunc(vals))      
# print(np.fix(vals))

# a = np.array([5, 10, 15, 20])
# b = np.array([6,  9, 15, 18])

# print(np.greater(a, b))
# print(np.less_equal(a, b))
# print(np.equal(a, b))
# print(np.maximum(a, b))
# print(np.minimum(a, b))


# x = np.array([True, False, True, False])
# y = np.array([True, True,  False, False])

# print(np.logical_and(x, y))
# print(np.logical_or(x, y))
# print(np.logical_not(x, y))


# print(np.pi)
# print(np.e)
# print(np.inf)
# print(-np.inf)
# print(np.nan)
# # print(np.PINF) # inf  (alias)
# # print(np.NINF) # -inf  (alias)
# # print(np.PZERO) #0.0
# print(np.euler_gamma)

# print(np.finfo(float).max)
# print(np.finfo(float).eps)
# print(np.iinfo(np.int32).max)
# print(np.iinfo(np.int8).min)

# data = np.array([1.0, np.nan, 3.0, np.inf, 5.0, -np.inf])

# print(np.isnan(data))
# print(np.isinf(data))
# print(np.isfinite(data))

# clean = np.nan_to_num(data, nan=0.0, posinf=999, neginf=-999)
# print(clean)

# data2 = np.array([10.0, np.nan, 30.0, np.nan, 50.0])
#
# print(np.nanmean(data2))
# print(np.nansum(data2))
# print(np.nanmax(data2))
# print(np.nanstd(data2))

# heights = np.array([162, 175, 158, 180, 171, 169, 185, 163, 177, 174])

# print(np.mean(heights))
# print(np.median(heights))

# print(np.std(heights))
# print(np.var(heights))
# print(np.ptp(heights)) #peak-to-peak (max - min)

# print(np.percentile(heights, 25)) #q1
# print(np.percentile(heights, 50)) #q2
# print(np.percentile(heights, 75)) #q3
#
# q1 = np.percentile(heights, 25)
# q3 = np.percentile(heights, 75)
#
# iqr = q3 - q1
# print(f"IQR: {iqr}")
#
# lower = q1 - 1.5 * iqr
# upper = q3 + 1.5 * iqr
# outliers = heights[(heights < lower) | (heights > upper)]
# print(f"Outliers: {outliers}")

# data = np.array([10, 20, 30, 40, 50])
#
# print(np.std(data, ddof=0)) #Entire Population
# print(np.std(data, ddof=1)) # Sample data


# study_hours  = np.array([2, 4, 6, 8, 10, 3, 7, 5])
# exam_scores  = np.array([50, 65, 75, 85, 95, 55, 80, 70])
#
# corr_matrix = np.corrcoef(study_hours, exam_scores)
# print(corr_matrix)
#
# r = corr_matrix[0, 1]
# print(f"Correlation: {r:.3f}")
#
# cov_matrix = np.cov(study_hours, exam_scores)
# print(cov_matrix)

# sales = np.array([100, 200, 150, 300, 250])
#
# print(np.cumsum(sales))
# print(np.cumprod(np.array([1,2,3,4,5])))
#
# prices = np.array([100, 105, 98, 112, 108])
# print(np.diff(prices))
# print(np.diff(prices, n=2))

#OLD METHOD
# np.random.seed(42)
# print(np.random.rand(5))

#NEW METHOD

# rng = np.random.default_rng(seed=42)
# print(rng.random(5))
# print(rng.integers(1, 101, size=10))

# u1 = rng.random(1000)
#
# u2 = rng.uniform(low=50, high=100, size=500)
# print(f"Mean: {u2.mean():.1f}")

# dice = rng.integers(1, 7, size=10)
# print(dice)

# heights = rng.normal(loc=170, scale=10, size=1000)
#
# print(f"Mean: {heights.mean():.2f}")
# print(f"Std : {heights.std():.2f}")
# print(f"Min : {heights.min():.2f}")
# print(f"Max : {heights.max():.2f}")

# within_1sd = np.sum(np.abs(heights - 170) < 10) / 1000
# within_2sd = np.sum(np.abs(heights - 170) < 20) / 1000
# within_3sd = np.sum(np.abs(heights - 170) < 30) / 1000
# print(f"Within 1σ: {within_1sd:.1%}")
# print(f"Within 2σ: {within_2sd:.1%}")
# print(f"Within 3σ: {within_3sd:.1%}")

# coin_flips = rng.binomial(n=10, p=0.5, size=1000)
# print(f"Avg heads per 10 flips: {coin_flips.mean():.1f}")
#
# clicks = rng.binomial(n=1, p=0.30, size=1000)
# print(f"Total clicks: {clicks.sum()}")
# print(f"Click rate:   {clicks.mean():.1%}")

# arrivals = rng.poisson(lam=180, size=1000)
# # print(arrivals)
# print(f"Busiest hour: {arrivals.max()} customers")
# print(f"Quietest:     {arrivals.min()} customers")
# print(f"Daily total:  {arrivals.sum()} customers")

# wait_times = rng.exponential(scale=5, size=100)
# print(wait_times)
#
# conversion = rng.beta(a=2, b=8, size=1000)
# print(conversion)
#
# arr = np.arange(1, 11)
# rng.shuffle(arr)
# print(arr)

# items = np.array(['A','B','C','D','E','F','G','H','I','J'])
# sample = rng.choice(items, size=5, replace=False)
# print(sample)

scores = np.array([72, 55, 88, 91, 60, 78, 45, 95])

# print(np.sort(scores))
# print(np.sort(scores)[::-1])
#
# idx = np.argsort(scores)
# print(idx)

# ranked = np.argsort(scores)[::-1]
#
# for rank, i in enumerate(ranked, 1):
#     print(f"Rank {rank}: Student {i + 1} — {scores[i]}")

# data = np.array([[3, 80], [1, 95], [2, 70], [4, 88]])
# sorted_by_score = data[np.argsort(data[:,1])[::-1]]
# print(sorted_by_score)

# arr = np.array([10, 20, 30, 40, 50, 30, 60, 30])
#
# idx = np.where(arr == 30)
# print(idx)
#
# result = np.where(arr > 30, 'High', 'Low')
# print(result)
#
# sorted_arr = np.array([10, 20, 30, 40, 50])
# pos = np.searchsorted(sorted_arr, 35)
# print(pos)
#
# mask = np.array([0, 5, 0, 3, 0, 8])
# print(np.nonzero(mask))
#
# print(np.any(arr > 55))
# print(np.all(arr > 5))
# print(np.all(arr > 15))

# a = np.array([1, 2, 3, 4, 5, 2, 3])
# b = np.array([3, 4, 5, 6, 7])
#
# print(np.unique(a))
#
# vals, counts = np.unique(a, return_counts=True)
# print(vals)
# print(counts)
#
# print(np.union1d(a, b))
# print(np.intersect1d(a, b))
# print(np.setdiff1d(a, b))
# print(np.setxor1d(a, b))
# # print(np.in1d(a, b))
#
# product_A_buyers = np.array([101,102,103,104,105])
# product_B_buyers = np.array([103,105,106,107])
# both = np.intersect1d(product_A_buyers, product_B_buyers)
# print(f"Bought both: Customer IDs {both}")


