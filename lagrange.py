def get_input(prompt, type_func=float):
    while True:
        try:
            return type_func(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")

# Objective function
def z(x, y):
    return 4*x**2 - 2*x*y + 6*y**2

# Partial derivatives
def dz_dx(x, y, lam):
    return 8*x - 2*y - lam

def dz_dy(x, y, lam):
    return -2*x + 12*y - lam

def constraint(x, y, target):
    return x + y - target

# Solve using substitution method for this specific problem
def solve_lagrange(target):
    # Starting with an initial guess:
    x = y = target / 2
    lam = 0

    # This method assumes the partial derivatives are equal to zero
    # and substitutes x from the constraint into the dz_dx equation
    # to solve for y and λ.
    y = (8 * target) / 10
    x = target - y
    lam = 8*x - 2*y

    return x, y, lam

# Constraint target
target = 72

# Solve the optimization problem
x_opt, y_opt, lam_opt = solve_lagrange(target)

# Calculate the optimal value of the objective function
z_opt = z(x_opt, y_opt)

print(f"Optimal x: {x_opt}")
print(f"Optimal y: {y_opt}")
print(f"Lagrange multiplier (λ): {lam_opt}")
print(f"Optimal value of the objective function (z): {z_opt}")
