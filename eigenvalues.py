def get_input(prompt, type_func=float):
    while True:
        try:
            return type_func(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")

def calculate_eigenvalues(matrix):
    a = matrix[0][0]
    b = matrix[0][1]
    c = matrix[1][0]
    d = matrix[1][1]
    trace = a + d
    determinant = a * d - b * c
    discriminant = trace**2 - 4 * determinant
    if discriminant < 0:
        return None  # Complex eigenvalues
    sqrt_discriminant = discriminant**0.5
    return [(trace + sqrt_discriminant) / 2, (trace - sqrt_discriminant) / 2]

def calculate_eigenvectors(matrix, eigenvalues):
    eigenvectors = []
    for eigenvalue in eigenvalues:
        a = matrix[0][0] - eigenvalue
        b = matrix[0][1]
        c = matrix[1][0]
        d = matrix[1][1] - eigenvalue

        # Solving (A - λI)v = 0
        if a != 0 or b != 0:
            if a == 0:
                eigenvector = [1, 0]  # If a is zero, b must be non-zero
            else:
                eigenvector = [-b / a, 1]
        elif c != 0 or d != 0:
            if c == 0:
                eigenvector = [1, 0]  # If c is zero, d must be non-zero
            else:
                eigenvector = [-d / c, 1]
        else:
            eigenvector = [1, 0]  # If both a and c are zero

        eigenvectors.append(eigenvector)
    return eigenvectors

# Input matrix
matrix = [[get_input("Enter element [0][0]: "),
           get_input("Enter element [0][1]: ")],
          [get_input("Enter element [1][0]: "),
           get_input("Enter element [1][1]: ")]]

eigenvalues = calculate_eigenvalues(matrix)

if eigenvalues:
    eigenvectors = calculate_eigenvectors(matrix, eigenvalues)
    print("Eigenvalues:", eigenvalues)
    print("Eigenvectors:", eigenvectors)
else:
    print("Complex eigenvalues, which cannot be handled by this script.")


