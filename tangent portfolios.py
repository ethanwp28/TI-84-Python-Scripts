def get_input(prompt, type_func=float):
    return type_func(input(prompt))

def get_list_input(prompt, length, type_func=float):
    return [get_input(f"{prompt} {i+1}: ", type_func) for i in range(length)]

def portfolio_std_dev(weights, std_devs, covariances, num_assets):
    variance = 0
    for i in range(num_assets):
        for j in range(num_assets):
            if i == j:
                variance += (weights[i] * std_devs[i])**2
            else:
                covariance_key = (min(i, j), max(i, j))
                variance += weights[i] * weights[j] * covariances.get(covariance_key, 0)
    return variance**0.5

def portfolio_return(weights, expected_returns):
    return sum(w * r for w, r in zip(weights, expected_returns))

def calculate_sharpe_ratio(weights, expected_returns, std_devs, covariances, risk_free_rate, num_assets):
    return (portfolio_return(weights, expected_returns) - risk_free_rate) / portfolio_std_dev(weights, std_devs, covariances, num_assets)

# Linear Congruential Generator for pseudo-random numbers
def lcg_rand():
    global lcg_seed
    a = 1664525
    c = 1013904223
    m = 2**32
    lcg_seed = (a * lcg_seed + c) % m
    return lcg_seed / m

# Initialize the random seed
lcg_seed = 123456789

# Get the number of assets
num_assets = get_input("Enter the number of assets: ", int)

# Get inputs for each asset
expected_returns = get_list_input("Enter expected return for asset", num_assets)
std_devs = get_list_input("Enter standard deviation for asset", num_assets)

# Get covariances
covariances = {}
for i in range(num_assets):
    for j in range(i + 1, num_assets):
        covariance = get_input(f"Enter covariance between asset {i+1} and asset {j+1}: ")
        covariances[(i, j)] = covariance
        covariances[(j, i)] = covariance

# Get risk-free rate
risk_free_rate = get_input("Enter the risk-free rate: ")

# Simple optimization to find the weights for maximum Sharpe ratio
best_sharpe_ratio = float('-inf')
best_weights = None
for _ in range(10000):  # Iterate a large number of times
    # Generate random weights using lcg_rand
    weights = [lcg_rand() for _ in range(num_assets)]
    total = sum(weights)
    weights = [w / total for w in weights]  # Normalize weights to sum to 1

    # Calculate Sharpe ratio
    sharpe_ratio = calculate_sharpe_ratio(weights, expected_returns, std_devs, covariances, risk_free_rate, num_assets)
    if sharpe_ratio > best_sharpe_ratio:
        best_sharpe_ratio = sharpe_ratio
        best_weights = weights

# Calculate final portfolio metrics
final_portfolio_return = portfolio_return(best_weights, expected_returns)
final_portfolio_std_dev = portfolio_std_dev(best_weights, std_devs, covariances, num_assets)

# Display the results
print("Optimal weights:", best_weights)
print("Tangent Portfolio Sharpe Ratio:", best_sharpe_ratio)
print("Expected Portfolio Return:", final_portfolio_return)
print("Portfolio Standard Deviation:", final_portfolio_std_dev)

