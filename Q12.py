def get_input(prompt, type_func=float):
    while True:
        try:
            return type_func(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")

# Constants
risk_free_rate = 0.03
market_return = 0.10
market_variance = 4
alphas = [1, 2, 2]
betas = [0.5, 1, 2]
residual_variances = [1, 1, 1]

# Number of assets
n_assets = len(alphas)

# Calculate expected returns for each asset
expected_returns = [alpha + beta * (market_return - risk_free_rate) for alpha, beta in zip(alphas, betas)]

# Build covariance matrix using Single Index Model
covariance_matrix = []
for i in range(n_assets):
    row = []
    for j in range(n_assets):
        if i == j:
            # Variance of asset i
            row.append(betas[i] * betas[j] * market_variance + residual_variances[i])
        else:
            # Covariance between asset i and j
            row.append(betas[i] * betas[j] * market_variance)
    covariance_matrix.append(row)

# Display covariance matrix and expected returns
print("Covariance Matrix:")
for row in covariance_matrix:
    print(row)
print("Expected Returns:", expected_returns)
