def get_input(prompt, type_func=float):
    while True:
        try:
            return type_func(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")

def cholesky_decomposition(matrix):
    n = len(matrix)
    L = [[0.0] * n for _ in range(n)]

    for i in range(n):
        for j in range(i + 1):
            temp_sum = sum(L[i][k] * L[j][k] for k in range(j))
            
            if i == j:  # Diagonal elements
                if matrix[i][i] - temp_sum <= 0:
                    raise ValueError("Matrix is not positive definite")
                L[i][j] = (matrix[i][i] - temp_sum) ** 0.5
            else:
                if L[j][j] == 0:
                    raise ValueError("Division by zero")
                L[i][j] = (matrix[i][j] - temp_sum) / L[j][j]
    return L

def input_matrix(n):
    return [[get_input(f"Enter element [{i}][{j}]: ") for j in range(n)] for i in range(n)]

# Get the size of the matrix from the user
n = int(get_input("Enter the size of the matrix: ", int))

# Input the matrix
print("Enter the elements of the matrix:")
Sigma = input_matrix(n)

try:
    L = cholesky_decomposition(Sigma)
    print("L (lower triangular matrix):")
    for row in L:
        print(row)
    
    # Reconstruct the matrix to verify decomposition
    Sigma_new = [[sum(L[i][k] * L[j][k] for k in range(n)) for j in range(n)] for i in range(n)]
    print("Reconstructed covariance matrix (Σ):")
    for row in Sigma_new:
        print(row)

except ValueError as e:
    print(str(e))
