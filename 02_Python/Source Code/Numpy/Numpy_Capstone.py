import numpy as np

# Array Fundamentals for ML Data

prices = np.array([250, 310, 190, 405, 275, 330, 220, 500])
houses = np.array([[1400,3,10],[1600,3,15],[1100,2,5],[2200,4,20],[1800,3,8]])

print(houses.shape, houses.dtype, houses.ndim)

weights = np.zeros((3, 1))
bias_col = np.ones((5, 1))
I = np.eye(4)
x_vals = np.linspace(0, 10, 50)
sample_ids = np.arange(20)

print(houses[2])

sqft = houses[:, 0]
batch = houses[:3]
big_houses = houses[houses[:, 1] > 3]
val_samples = houses[[0, 2, 4]]
reversed_houses = houses[::-1]

image = pixels.reshape(10, 10)
flat = feature_map.flatten()
prices_col = prices.reshape(-1, 1)
weights_T = weights.T
full_data = np.vstack([batch1, batch2])
features = np.hstack([sqft.reshape(-1,1), age.reshape(-1,1)])
