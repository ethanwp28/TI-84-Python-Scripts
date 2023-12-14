def get_input(prompt, type_func=float):
    return type_func(input(prompt))

def get_list_input(prompt, length, type_func=float):
    return [get_input(f"{prompt} {i+1}: ", type_func) for i in range(length)]

def minimal_variance_portfolio(expected_return_A, expected_return_B, std_dev_A, std_dev_B, correlation):
    covariance = correlation * std_dev_A * std_dev_B

    weight_A = (std_dev_B**2 - covariance) / (std_dev_A**2 + std_dev_B**2 - 2 * covariance)
    weight_B = 1 - weight_A

    expected_return = weight_A * expected_return_A + weight_B * expected_return_B

    portfolio_variance = (weight_A * std_dev_A)**2 + (weight_B * std_dev_B)**2 + 2 * weight_A * weight_B * covariance
    portfolio_std_dev = (portfolio_variance)**0.5

    return expected_return, portfolio_std_dev

# Get inputs from user
expected_return_A = get_input("expected return for Asset A: ")
expected_return_B = get_input("expected return for Asset B: ")
std_dev_A = get_input("standard deviation for Asset A: ")
std_dev_B = get_input("standard deviation for Asset B: ")
num_correlations = get_input("number of different correlations: ", int)
correlations = get_list_input("Enter correlation", num_correlations)

# Calculate and display results for each correlation
for corr in correlations:
    expected_return, portfolio_std_dev = minimal_variance_portfolio(expected_return_A, expected_return_B, std_dev_A, std_dev_B, corr)
    print(f"Correlation: {corr}")
    print(f"Expected Return: {expected_return}, Portfolio Std Dev: {portfolio_std_dev}")
