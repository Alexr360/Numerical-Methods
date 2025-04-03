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

def jacobi_iteration(A, b, x_init, num_iterations):
    x = x_init.copy()
    results = []
    for _ in range(num_iterations):
        x_new = np.zeros_like(x)
        x_new[0] = (b[0] - A[0, 1] * x[1]) / A[0, 0]
        x_new[1] = (b[1] - A[1, 0] * x[0]) / A[1, 1]
        x[:] = x_new
        results.append(x.copy())
    return results

def gauss_seidel_iteration(A, b, x_init, num_iterations):
    x = x_init.copy()
    results = []
    for _ in range(num_iterations):
        x[0] = (b[0] - A[0, 1] * x[1]) / A[0, 0]
        x[1] = (b[1] - A[1, 0] * x[0]) / A[1, 1]
        results.append(x.copy())
    return results

jacobi_results = jacobi_iteration(A, b, x_jacobi, num_iterations)
gauss_seidel_results = gauss_seidel_iteration(A, b, x_gauss_seidel, num_iterations)

print("Jacobi Iteration Results:")
for i, result in enumerate(jacobi_results, start=1):
    print(f"Iteration {i}: {result}")

print("\nGauss-Seidel Iteration Results:")
for i, result in enumerate(gauss_seidel_results, start=1):
    print(f"Iteration {i}: {result}")