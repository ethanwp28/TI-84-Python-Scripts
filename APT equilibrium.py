def get_input(prompt, type_func=float):
    while True:
        try:
            return type_func(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")

# Function to calculate the determinant of a 3x3 matrix
def determinant_3x3(matrix):
    return (matrix[0][0] * (matrix[1][1]*matrix[2][2] - matrix[1][2]*matrix[2][1]) -
            matrix[0][1] * (matrix[1][0]*matrix[2][2] - matrix[1][2]*matrix[2][0]) +
            matrix[0][2] * (matrix[1][0]*matrix[2][1] - matrix[1][1]*matrix[2][0]))

# Function to replace column in 3x3 matrix and calculate determinant
def det_with_replaced_column(matrix, column, replacement):
    modified_matrix = [row[:] for row in matrix]
    for i in range(3):
        modified_matrix[i][column] = replacement[i]
    return determinant_3x3(modified_matrix)

# Get user input for beta matrix values
beta_matrix = []
for i in range(3):
    row = [get_input(f"Enter beta value for row {i+1}, column 1: "),
           get_input(f"Enter beta value for row {i+1}, column 2: "),
           get_input(f"Enter beta value for row {i+1}, column 3: ")]
    beta_matrix.append(row)

# Get user input for return vector values
return_vector = [get_input("Enter return value 1: "),
                 get_input("Enter return value 2: "),
                 get_input("Enter return value 3: ")]

# Calculate lambda values using Cramer's Rule
main_det = determinant_3x3(beta_matrix)
lambda_values = []
for i in range(3):
    lambda_values.append(det_with_replaced_column(beta_matrix, i, return_vector) / main_det)

lambda_0, lambda_1, lambda_2 = lambda_values

print("Lambda 0:", lambda_0)
print("Lambda 1:", lambda_1)
print("Lambda 2:", lambda_2)