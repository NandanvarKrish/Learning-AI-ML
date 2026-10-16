import numpy as np

def evaluate_regression(y_true, y_pred):
    ss_res = ((y_true - y_pred)**2).sum()
    ss_tot = ((y_true - y_true.mean())**2).sum()
    r2   = 1 - ss_res / ss_tot
    rmse = np.sqrt(((y_true - y_pred)**2).mean())
    mae  = np.abs(y_true - y_pred).mean()
    return r2, rmse, mae

def kmeans(X, k, max_iter=100, seed=42):
    rng_km = np.random.default_rng(seed)

    init_idx  = rng_km.choice(len(X), size=k, replace=False)
    centroids = X[init_idx].copy()
    labels = np.zeros(len(X), dtype=int)
    history = []

    for iteration in range(max_iter):
        diff  = X[:, np.newaxis, :] - centroids[np.newaxis, :, :]
        dists = np.sqrt((diff**2).sum(axis=2))
        new_labels = dists.argmin(axis=1)

        new_centroids = np.array([
            X[new_labels == j].mean(axis=0) if (new_labels==j).any()
            else centroids[j]
            for j in range(k)
        ])

        inertia = sum(
            ((X[new_labels==j] - new_centroids[j])**2).sum()
            for j in range(k) if (new_labels==j).any()
        )
        history.append(inertia)

        if np.array_equal(new_labels, labels):
            print(f"Converged at iteration {iteration+1}")
            break

        labels, centroids = new_labels, new_centroids

    return labels, centroids, history

def relu(x):
    return np.maximum(0, x)

def he_init(fan_in, fan_out):
    return rng.normal(0, np.sqrt(2/fan_in), (fan_in, fan_out))

def forward_pass(X):
    Z1 = X  @ W1 + b1
    A1 = relu(Z1)
    Z2 = A1 @ W2 + b2
    A2 = relu(Z2)
    Z3 = A2 @ W3 + b3
    return Z3.flatten()

rng = np.random.default_rng(2027)
n = 1000

size_sqft = rng.normal(1500, 400, n).clip(500, 4000)
bedrooms = rng.integers(1, 6, n).astype(float)
bathrooms = rng.choice([1, 1.5, 2, 2.5, 3], n)
age_years = rng.integers(1, 51, n).astype(float)
garage_cars = rng.integers(0, 4, n).astype(float)
dist_school = rng.exponential(2, n).clip(0.1, 15)
crime_rate = rng.beta(2, 8, n) * 100
has_pool = rng.binomial(1, 0.2, n).astype(float)

print(size_sqft.shape)
print(bedrooms.shape)
print(bathrooms.shape)
print(age_years.shape)
print(garage_cars.shape)
print(dist_school.shape)
print(crime_rate.shape)
print(has_pool.shape)

X_raw = np.column_stack([size_sqft, bedrooms, bathrooms,
                         age_years, garage_cars, dist_school,
                         crime_rate, has_pool])

feature_names = ['size','beds','baths','age','garage','school_dist','crime','pool']

true_weights = np.array([150, 8000, 12000, -500, 5000, -3000, -800, 20000])
true_bias    = 50000
noise        = rng.normal(0, 15000, n)
y_raw        = X_raw @ true_weights + true_bias + noise

print(f"X shape: {X_raw.shape}")
print(f"y shape: {y_raw.shape}")
print(f"Price range: ${y_raw.min():,.0f} – ${y_raw.max():,.0f}")

X_mean = X_raw.mean(axis=0, keepdims=True)
X_std  = X_raw.std(axis=0,  keepdims=True)
X_norm = (X_raw - X_mean) / X_std
print(f"Normalised mean ≈ 0: {X_norm.mean(axis=0).round(4)}")
print(f"Normalised std  = 1: {X_norm.std(axis=0).round(4)}")

idx = rng.permutation(n)
split = int(n * 0.8)
train_idx, test_idx = idx[:split], idx[split:]

X_train, X_test = X_norm[train_idx], X_norm[test_idx]
y_train, y_test = y_raw[train_idx],  y_raw[test_idx]

np.savez('train.npz', X=X_train, y=y_train)
np.savez('test.npz',  X=X_test,  y=y_test)
print(f"Train: {X_train.shape}, Test: {X_test.shape}")

X_b = np.column_stack([np.ones(len(X_train)), X_train])

w_opt, _, _, _ = np.linalg.lstsq(X_b, y_train, rcond=None)
bias, weights = w_opt[0], w_opt[1:]

X_test_b = np.column_stack([np.ones(len(X_test)), X_test])
y_pred_lr = X_test_b @ w_opt

print("Learned weights:")
for name, w in zip(['bias'] + feature_names, w_opt):
    print(f"  {name:12s}: {w:+.2f}")

alpha  = 0.001
epochs = 10000
m      = len(X_train)

w_gd  = np.zeros(X_b.shape[1])
loss_history = []

for i in range(epochs):
    y_hat = X_b @ w_gd
    error = y_hat - y_train
    loss  = (error**2).mean() 
    grad  = (X_b.T @ error) / m 
    w_gd -= alpha * grad

    if i % 100 == 0:
        loss_history.append(loss)
        print(f"Epoch {i:4d}: MSE = {loss:,.0f}")

print(f"\nlstsq vs GD weight difference: {np.linalg.norm(w_opt - w_gd):.2f}")

r2, rmse, mae = evaluate_regression(y_test, y_pred_lr)
print(f"R²   = {r2:.4f}")
print(f"RMSE = ${rmse:,.0f}")
print(f"MAE  = ${mae:,.0f}")

labels, centroids, history = kmeans(X_norm, k=4)

for k_i in range(4):
    cluster_prices = y_raw[labels == k_i]
    print(f"Cluster {k_i}: {(labels==k_i).sum()} houses, avg price ${cluster_prices.mean():,.0f}")

W1 = he_init(8,  16);  b1 = np.zeros(16)
W2 = he_init(16, 8);   b2 = np.zeros(8)
W3 = he_init(8,  1);   b3 = np.zeros(1)

y_pred_nn = forward_pass(X_test)
r2_nn, rmse_nn, mae_nn = evaluate_regression(y_test, y_pred_nn)
print(f"NN (untrained) R²={r2_nn:.4f}, RMSE=${rmse_nn:,.0f}")

Z1_einsum = np.einsum('ni,ij->nj', X_test, W1) + b1
print(f"einsum matches matmul: {np.allclose(X_test@W1, Z1_einsum)}")

params = [(W1,b1,'Layer1'),(W2,b2,'Layer2'),(W3,b3,'Layer3')]
total_params = 0

for W, b, name in params:
    p = W.size + b.size
    total_params += p
    print(f"{name}: W{W.shape} + b{b.shape} = {p} params")

print(f"Total: {total_params} params = {total_params*8} bytes ({total_params*8/1024:.1f} KB)")

np.savez('linear_model.npz',
          weights=weights, bias=np.array([bias]),
          X_mean=X_mean, X_std=X_std)

results = np.column_stack([y_test, y_pred_lr, y_test - y_pred_lr])
np.savetxt('predictions.csv', results,
           delimiter=',', header='actual,predicted,residual',
           fmt='%.2f', comments='')

np.save('cluster_labels.npy', labels)
print("All results saved to disk ✅")

model_data = np.load('linear_model.npz')
print(f"Loaded weights: {model_data['weights'].round(2)}")
