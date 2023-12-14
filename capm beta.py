def get_input(prompt, type_func=float):
    while True:
        try:
            return type_func(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")

# Input parameters
risk_free_rate = get_input("Enter the risk-free rate: ")
expected_return_market = get_input("Enter the expected market return: ")
beta = get_input("Enter the beta: ")

# Now you can use these inputs in further calculations as needed
# For example, if you're calculating the expected return using the CAPM:
expected_return = risk_free_rate + beta * (expected_return_market - risk_free_rate)

print("Expected Return:", expected_return)
