import numpy as np

rng = np.random.default_rng(2024)

n_users, n_movies = 50, 20

movies = ['Inception','Interstellar','The Matrix','Avatar','Dune',
          'Oppenheimer','Barbie','Parasite','1917','Joker',
          'Tenet','Knives Out','Get Out','Mad Max','Blade Runner',
          'Everything Everywhere','Top Gun','Spider-Man','Dr Strange','Dune 2']

raw = rng.integers(1, 6, size=(n_users, n_movies))

mask = rng.random((n_users, n_movies)) > 0.4
R = raw * mask 

print(f"Shape: {R.shape}")
print(f"Sparsity: {(R==0).mean():.1%} zeros")
print(f"First user ratings: {R[0]}")

movie_sums   = R.sum(axis=0)
movie_counts = (R > 0).sum(axis=0)
movie_avgs   = np.where(movie_counts > 0, movie_sums / movie_counts, 0)
best_movie   = movies[np.argmax(movie_avgs)]
print(f"Most popular movie: {best_movie} ({movie_avgs.max():.2f}★)")

R_float = R.astype(float)
R_float[R_float == 0] = np.nan

user_means = np.nanmean(R_float, axis=1, keepdims=True) 
R_centred  = R_float - user_means
R_centred  = np.nan_to_num(R_centred, nan=0.0)

U, s, Vt = np.linalg.svd(R_centred, full_matrices=False)

k = 5
R_approx = U[:, :k] @ np.diag(s[:k]) @ Vt[:k, :]
R_predicted = R_approx + user_means
R_predicted = np.clip(R_predicted, 1, 5)

explained = (s[:k]**2).sum() / (s**2).sum()
print(f"Variance explained by k={k} factors: {explained:.1%}")

user_id = 0
unwatched = R[user_id] == 0 
pred_scores = R_predicted[user_id].copy()
pred_scores[~unwatched] = -np.inf 
top5 = np.argsort(pred_scores)[-5:][::-1]
print(f"\nTop 5 recommendations for User {user_id}:")
for rank, idx in enumerate(top5, 1):
    print(f"  {rank}. {movies[idx]} → Predicted: {pred_scores[idx]:.2f}★")

norms = np.linalg.norm(R_centred, axis=1, keepdims=True)
norms = np.where(norms == 0, 1, norms)  
R_norm = R_centred / norms 

# Full similarity matrix — ONE matrix multiply!
sim_matrix = R_norm @ R_norm.T
print(f"Similarity matrix shape: {sim_matrix.shape}")

sim_to_user0 = sim_matrix[0].copy()
sim_to_user0[0] = -1
similar_users = np.argsort(sim_to_user0)[-3:][::-1]
print(f"Users most similar to User 0: {similar_users}")
print(f"Similarity scores: {sim_to_user0[similar_users].round(3)}")

cov = np.cov(R_centred)  
evals, evecs = np.linalg.eigh(cov) 
order = np.argsort(evals)[::-1]
evals = evals[order]; evecs = evecs[:, order]

# users_2d = R_centred @ evecs[:, :2]
explained_var = evals[:2] / evals[evals > 0].sum() * 100
print(f"PC1 explains: {explained_var[0]:.1f}%")
print(f"PC2 explains: {explained_var[1]:.1f}%")
# print(f"2D user positions (first 5):\n{np.round(users_2d[:5],2)}")

A_price = np.array([
    [1,  1,  1,  1],
    [2, -1,  1, -1],
    [1,  3, -1,  1],
    [1, -1,  2,  3]
], dtype=float)

b_price = np.array([100, 20, 60, 50], dtype=float)

print(f"det = {np.linalg.det(A_price):.2f}")
print(f"rank = {np.linalg.matrix_rank(A_price)}") 

prices = np.linalg.solve(A_price, b_price)
tier_names = ['Basic', 'Standard', 'Premium', 'Family']
print("\nOptimal Subscription Prices:")
for name, price in zip(tier_names, prices):
    print(f"  {name}: ₹{np.abs(price):.2f}/month")

print(f"Verify: {np.allclose(A_price @ prices, b_price)}")