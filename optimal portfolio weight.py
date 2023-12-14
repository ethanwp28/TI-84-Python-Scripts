def get_input(prompt, type_func=float):
    while True:
        try:
            return type_func(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_portfolio_variance(weights, cov_matrix, num_assets):
    variance = 0
    for i in range(num_assets):
        for j in range(num_assets):
            variance += weights[i] * weights[j] * cov_matrix[i][j]
    return variance

def get_portfolio_return(weights, returns):
    return sum(w * r for w, r in zip(weights, returns))

# Get user input for the number of assets (up to 3)
num_assets = int(get_input("Enter the number of assets (up to 3): ", int))
while num_assets < 1 or num_assets > 3:
    print("Please enter a number between 1 and 3.")
    num_assets = int(get_input("Enter the number of assets (up to 3): ", int))

# Get user inputs for expected returns and standard deviations
expected_returns = [get_input(f"Enter expected return for asset {i+1}: ") for i in range(num_assets)]
std_devs = [get_input(f"Enter standard deviation for asset {i+1}: ") for i in range(num_assets)]

# Initialize covariance matrix
cov_matrix = [[0 for _ in range(num_assets)] for _ in range(num_assets)]

# Fill in the covariance matrix
for i in range(num_assets):
    for j in range(i, num_assets):
        if i == j:
            cov_matrix[i][j] = std_devs[i] ** 2
        else:
            cov_ij = get_input(f"Enter covariance between assets {i+1} and {j+1}: ")
            cov_matrix[i][j] = cov_matrix[j][i] = cov_ij

# Get user input for target return
target_return = get_input("Enter target return as a decimal (e.g., 0.15 for 15%): ")

# Optimization process
min_variance = float('inf')
optimal_weights = []

def check_and_update_optimal():
    global optimal_weights, min_variance
    if abs(portfolio_return - target_return) < 0.005:  # Tolerance for target return
        variance = get_portfolio_variance(weights, cov_matrix, num_assets)
        if variance < min_variance:
            min_variance = variance
            optimal_weights = weights

# Brute-force search for optimal weights
for w1 in range(101):
    for w2 in range(101 - w1):
        if num_assets == 2:
            weights = [w1 / 100.0, w2 / 100.0]
            portfolio_return = get_portfolio_return(weights, expected_returns)
            check_and_update_optimal()

        elif num_assets == 3:
            w3 = 100 - w1 - w2
            weights = [w1 / 100.0, w2 / 100.0, w3 / 100.0]
            portfolio_return = get_portfolio_return(weights, expected_returns)
            check_and_update_optimal()


# Display results
if optimal_weights:
    optimal_return = get_portfolio_return(optimal_weights, expected_returns)
    optimal_std_dev = min_variance ** 0.5
    print("Optimal Weights:", optimal_weights)
    print(f"Expected Return: {optimal_return:.2%}")
    print(f"Standard Deviation: {optimal_std_dev:.2%}")
else:
    print("No optimal portfolio found within the specified return target.")
