def get_input(prompt, type_func=float):
    while True:
        try:
            return type_func(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")

def calculate_portfolio_variance(N, avg_variance, avg_covariance):
    return (1/N) * (avg_variance - avg_covariance) + avg_covariance

# User inputs for average variance and covariance
avg_variance = get_input("Enter the average variance of return for an individual security: ")
avg_covariance = get_input("Enter the average covariance between the returns of the securities: ")

# User input for number of different portfolio sizes to analyze
num_portfolios = get_input("How many different portfolio sizes do you want to analyze? ", int)

# User inputs for different portfolio sizes
portfolio_sizes = [get_input(f"Enter size for portfolio {i+1}: ", int) for i in range(num_portfolios)]

# Calculating and displaying the expected variance for each portfolio size
for size in portfolio_sizes:
    variance = calculate_portfolio_variance(size, avg_variance, avg_covariance)
    print(f"Expected variance of portfolio with {size} securities: {variance}")
