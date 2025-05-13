def jacobi(A, b, x0=None, tol=1e-10, max_iterations=1000):
    n = len(A)
    # Initialize solution
    x = x0[:] if x0 is not None else [0.0 for _ in range(n)]

    for iteration in range(1, max_iterations + 1):
        x_new = x[:]
        for i in range(n):
            # Sum of A[i][j] * x[j] for j != i
            sum_ax = sum(A[i][j] * x[j] for j in range(n) if j != i)
            # Update rule: (b[i] - sum_ax) / A[i][i]
            x_new[i] = (b[i] - sum_ax) / A[i][i]

        # Check for convergence
        diff = max(abs(x_new[i] - x[i]) for i in range(n))
        if diff < tol:
            print(f"Converged in {iteration} iterations.")
            return x_new

        x = x_new

    print("Warning: Maximum iterations reached without convergence.")
    return x_new


# Example usage:
if __name__ == "__main__":
    # Example system:
    #  4x +  y +  z = 7
    #  x + 5y + 2z = -8
    # 2x +  y + 6z = 6
    A = [
        [4.0, 1.0, 1.0],
        [1.0, 5.0, 2.0],
        [2.0, 1.0, 6.0]
    ]
    b = [7.0, -8.0, 6.0]

    # Call Jacobi solver
    solution = jacobi(A, b, tol=1e-12, max_iterations=500)
    print("Solution:", solution)
