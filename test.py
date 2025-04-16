import numpy as np

def jacobi(A, b, x0=None, tol=1e-10, max_iter=100):
    n = len(A)
    x = x0 if x0 is not None else np.zeros(n)
    x_new = np.zeros(n)

    for _ in range(max_iter):
        for i in range(n):
            x_new[i] = (b[i] - np.dot(A[i, :], x) + A[i, i] * x[i]) / A[i, i]

        if np.linalg.norm(x_new - x, ord=np.inf) < tol:
            return x_new
        x = x_new.copy()

    return x_new  # Return after max_iter if no convergence

def gauss_seidel(A, b, x0=None, tol=1e-10, max_iter=100):
    n = len(A)
    x = x0 if x0 is not None else np.zeros(n)

    for _ in range(max_iter):
        x_old = x.copy()
        for i in range(n):
            x[i] = (b[i] - np.dot(A[i, :i], x[:i]) - np.dot(A[i, i+1:], x[i+1:])) / A[i, i]

        if np.linalg.norm(x - x_old, ord=np.inf) < tol:
            return x

    return x  # Return after max_iter if no convergence

def linear_regression(x, y):
    A = np.vstack([x, np.ones(len(x))]).T
    m, b = np.linalg.lstsq(A, y, rcond=None)[0]
    return m, b  # Returns slope (m) and intercept (b)

def polynomial_regression(x, y, degree=2):
    coeffs = np.polyfit(x, y, degree)
    return coeffs  # Returns polynomial coefficients

def power_law_fit(x, y):
    log_x, log_y = np.log(x), np.log(y)
    b, log_a = np.polyfit(log_x, log_y, 1)
    a = np.exp(log_a)
    return a, b  # Returns a and b for y = ax^b