def get_input(prompt, type_func=float):
    return type_func(input(prompt))

def get_list_input(prompt, length, type_func=float):
    return [get_input(f"{prompt} {i+1}: ", type_func) for i in range(length)]

def calculate_portfolio_variance(weights, std_devs, correlation):
    variance = 0
    for i in range(len(weights)):
        for j in range(len(weights)):
            covariance = correlation * std_devs[i] * std_devs[j] if i != j else std_devs[i]**2
            variance += weights[i] * weights[j] * covariance
    return variance

def calculate_portfolio_return(weights, returns):
    return sum(w * r for w, r in zip(weights, returns))

# Get inputs from user
num_assets = get_input("number of assets: ", int)
expected_returns = get_list_input("expected returns", num_assets)
std_devs = get_list_input("standard deviation", num_assets)
correlation = get_input("correlation")

# Portfolio weights
weights = get_list_input("weight", num_assets)

# Calculations
portfolio_variance = calculate_portfolio_variance(weights, std_devs, correlation)
portfolio_return = calculate_portfolio_return(weights, expected_returns)

# Display results
print("Variance:", portfolio_variance)
print("Expected Return:", portfolio_return)