import numpy as np

rng = np.random.default_rng(seed=2024)

companies = ['TechCo', 'HealthX', 'EnergyPlus', 'FinBank', 'RetailMart']
days = 504

start_prices = np.array([500, 250, 180, 320, 90])

daily_returns = rng.normal(loc=0.0005, scale=0.015, size=(504, 5))

print(daily_returns)

price_matrix = start_prices * np.cumprod(1 + daily_returns, axis=0)

print(f"Shape: {price_matrix.shape}")
print("First week prices:\n", np.round(price_matrix[:5], 2))

returns = np.diff(price_matrix, axis=0) / price_matrix[:-1] * 100
print(f"Returns shape: {returns.shape}")

annual_volatility = np.std(returns , axis=0) * np.sqrt(252)
print(f"Volatility: {annual_volatility}")

best_day = np.max(returns, axis=0)
worst_day = np.min(returns, axis=0)

positive_days = np.sum(returns > 0, axis=0)
negative_days = np.sum(returns < 0, axis=0)

for i, comp in enumerate(companies):
    print("=" * 30)
    print(f"Annual Volatility: {annual_volatility[i]:.2f}%")
    print(f"Best Single Day: {best_day[i]:.2f}%")
    print(f"Worst Single Day: {worst_day[i]:.2f}%")
    print(f"Green/Red Days : {positive_days[i]:.2f} Green / {negative_days[i]:.2f} Red")
    print("=" * 30)

window = 20
techco_prices = price_matrix[:, 0]
sma_20 = np.array([
    np.mean(techco_prices[i:i+window])
    for i in range(len(techco_prices) - window + 1)
])
window_50 = 50
sma_50 = np.array([
    np.mean(techco_prices[i:i+window_50])
    for i in range(len(techco_prices) - window_50 + 1)
])

sma_20_aligned = sma_20[30:]

corr_matrix = np.corrcoef(returns.T)
print(f"Correlation matrix:\n{corr_matrix}")

z_scores = (returns - np.mean(returns, axis=0)) / np.std(returns, axis=0) / np.std(returns, axis=0)

crash_days = np.sum(z_scores < -3, axis=0)
print(f"Crash Days per company : {crash_days}")

var_95 = np.percentile(returns, 5, axis=0)

for i, company in enumerate(companies):
    print(f"{company}: Worst Day loss = {var_95[i]:.2f}%")

portfolio_daily_returns = np.mean(returns, axis=1)
total_portfolio_return = (np.prod(1 + portfolio_daily_returns / 100) - 1) * 100
portfolio_annual_vol = np.std(portfolio_daily_returns) * np.sqrt(252)
sharpe_ratio = (np.mean(portfolio_daily_returns) * 252) / (portfolio_annual_vol)
total_returns_per_company = ((price_matrix[-1] - price_matrix[0]) / price_matrix[0]) * 100

best_company = companies[np.argmax(total_returns_per_company)]
riskiest_company = companies[np.argmax(annual_volatility)]

print("════════════════════════════════════════════════════")
print("          VERTEX CAPITAL — 2-YEAR REPORT            ")
print("════════════════════════════════════════════════════")
print("COMPANY PERFORMANCE:")
print(f"{'Company':<12} {'Start':<8} {'End':<8} {'Return':<10} {'Risk (σ)'}")
print("-" * 50)
for i, comp in enumerate(companies):
    print(f"{comp:<12} {price_matrix[0, i]:<8.1f} {price_matrix[-1, i]:<8.1f} {total_returns_per_company[i]:>+6.2f}%    {annual_volatility[i]:.2f}%")

print("\nSUMMARY HIGHLIGHTS:")
print(f"  • Winner (Best Return) : {best_company} ({np.max(total_returns_per_company):+.2f}%)")
print(f"  • Riskiest Asset       : {riskiest_company} ({np.max(annual_volatility):.2f}% Volatility)")

print("\nEQUAL-WEIGHT PORTFOLIO (20% Each):")
print(f"  • Total Return         : {total_portfolio_return:+.2f}%")
print(f"  • Annual Volatility    : {portfolio_annual_vol:.2f}%")
print(f"  • Sharpe Ratio         : {sharpe_ratio:.2f}")

print("\nANOMALIES DETECTED:")
print(f"  • Total Market Crash Days Across All Stocks: {np.sum(crash_days)}")
print("════════════════════════════════════════════════════")

