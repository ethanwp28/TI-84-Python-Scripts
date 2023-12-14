def get_input(prompt, type_func=float):
    while True:
        try:
            return type_func(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")

# Input parameters
a_A = get_input("Enter alpha for Asset A: ")
a_B = get_input("Enter alpha for Asset B: ")

b_A1 = get_input("Enter beta1 for Asset A: ")
b_B1 = get_input("Enter beta1 for Asset B: ")

b_A2 = get_input("Enter beta2 for Asset A: ")
b_B2 = get_input("Enter beta2 for Asset B: ")

sigma_c_A = get_input("Enter unsystematic risk for Asset A: ")
sigma_c_B = get_input("Enter unsystematic risk for Asset B: ")

I1 = get_input("Enter index value I1: ")
I2 = get_input("Enter index value I2: ")

sigma_I1 = get_input("Enter standard deviation for index I1: ")
sigma_I2 = get_input("Enter standard deviation for index I2: ")

# Calculations
expected_return_A = a_A + b_A1 * I1 + b_A2 * I2
expected_return_B = a_B + b_B1 * I1 + b_B2 * I2

variance_A = b_A1**2 * sigma_I1**2 + b_A2**2 * sigma_I2**2 + sigma_c_A**2
variance_B = b_B1**2 * sigma_I1**2 + b_B2**2 * sigma_I2**2 + sigma_c_B**2

covariance_AB = b_A1 * b_B1 * sigma_I1**2 + b_A2 * b_B2 * sigma_I2**2

# Output results
print("Expected Return A:", expected_return_A)
print("Expected Return B:", expected_return_B)
print("Variance A:", variance_A)
print("Variance B:", variance_B)
print("Covariance AB:", covariance_AB)
