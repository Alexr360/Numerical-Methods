import numpy as np

# Given system of equations:
# x0 + x1 = 10
# 2x0 + 4x1 = 28

# Coefficients matrix A and constants vector b
A = np.array([[1, 1], [2, 4]])
b = np.array([10, 28])

# Initial guess
x_jacobi = np.array([0.0, 0.0])
x_gauss_seidel = np.array([0.0, 0.0])

# Number of iterations
num_iterations = 3

# Jacobi Iteration
jacobi_results = []
for _ in range(num_iterations):
    x_new = np.zeros_like(x_jacobi)
    x_new[0] = (b[0] - A[0, 1] * x_jacobi[1]) / A[0, 0]
    x_new[1] = (b[1] - A[1, 0] * x_jacobi[0]) / A[1, 1]
    x_jacobi[:] = x_new
    jacobi_results.append(x_jacobi.copy())

# Gauss-Seidel Iteration
gauss_seidel_results = []
for _ in range(num_iterations):
    x_gauss_seidel[0] = (b[0] - A[0, 1] * x_gauss_seidel[1]) / A[0, 0]
    x_gauss_seidel[1] = (b[1] - A[1, 0] * x_gauss_seidel[0]) / A[1, 1]
    gauss_seidel_results.append(x_gauss_seidel.copy())

print("Jacobi Iteration Results:")
for i, result in enumerate(jacobi_results, start=1):
    print(f"Iteration {i}: {result}")

print("\nGauss-Seidel Iteration Results:")
for i, result in enumerate(gauss_seidel_results, start=1):
    print(f"Iteration {i}: {result}")