def gauss_seidel(A, b, x0=None, tol=1e-10, max_iterations=1000):
    n = len(A)
    # Initialize solution
    x = x0[:] if x0 is not None else [0.0 for _ in range(n)]

    for iteration in range(1, max_iterations + 1):
        x_new = x[:]
        for i in range(n):
            # Sum over known new values
            sum1 = sum(A[i][j] * x_new[j] for j in range(i))
            # Sum over old values
            sum2 = sum(A[i][j] * x[j] for j in range(i + 1, n))
            x_new[i] = (b[i] - sum1 - sum2) / A[i][i]

        # Check for convergence
        diff = max(abs(x_new[i] - x[i]) for i in range(n))
        if diff < tol:
            print(f"Converged in {iteration} iterations.")
            return x_new

        x = x_new

    print("Warning: Maximum iterations reached without convergence.")
    return x


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

    solution = gauss_seidel(A, b)
    print(f"Solution: {solution}")
