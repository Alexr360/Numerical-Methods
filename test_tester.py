import numpy as np
from test import jacobi, gauss_seidel, linear_regression, polynomial_regression, power_law_fit

def test_jacobi():
    # Test case 1: Simple 2x2 system
    A = np.array([[4, 1], [2, 3]])
    b = np.array([1, 2])
    x0 = np.array([0, 0])
    tol = 1e-6
    max_iter = 100
    result = jacobi(A, b, x0, tol, max_iter)
    expected = np.linalg.solve(A, b)
    assert np.allclose(result, expected, atol=tol), "Test case 1 failed"

    # Test case 2: Larger 3x3 system
    A = np.array([[10, -1, 2], [-1, 11, -1], [2, -1, 10]])
    b = np.array([6, 25, -11])
    x0 = np.array([0, 0, 0])
    tol = 1e-6
    max_iter = 100
    result = jacobi(A, b, x0, tol, max_iter)
    expected = np.linalg.solve(A, b)
    assert np.allclose(result, expected, atol=tol), "Test case 2 failed"

    # Test case 3: Non-converging system
    A = np.array([[1, 2], [2, 1]])
    b = np.array([3, 3])
    x0 = np.array([0, 0])
    tol = 1e-6
    max_iter = 10
    result = jacobi(A, b, x0, tol, max_iter)
    assert not np.allclose(result, np.linalg.solve(A, b), atol=tol), "Test case 3 failed"

def test_gauss_seidel():
    A = np.array([[4, 1], [2, 3]])
    b = np.array([1, 2])
    x0 = np.array([0, 0])
    tol = 1e-10
    max_iter = 1000
    result = gauss_seidel(A, b, x0, tol, max_iter)
    expected = np.linalg.solve(A, b)
    assert np.allclose(result, expected, atol=tol), "Gauss-Seidel test failed"

def test_linear_regression():
    x = np.array([1, 2, 3, 4, 5])
    y = np.array([2, 4, 6, 8, 10])
    m, b = linear_regression(x, y)
    assert np.isclose(m, 2) and np.isclose(b, 0), "Linear regression test failed"

def test_polynomial_regression():
    x = np.array([1, 2, 3, 4, 5])
    y = np.array([1, 4, 9, 16, 25])
    coeffs = polynomial_regression(x, y, degree=2)
    expected = np.array([1, 0, 0])  # y = x^2
    assert np.allclose(coeffs, expected, atol=1e-6), "Polynomial regression test failed"

def test_power_law_fit():
    x = np.array([1, 2, 3, 4, 5])
    y = np.array([1, 4, 9, 16, 25])
    a, b = power_law_fit(x, y)
    assert np.isclose(a, 1) and np.isclose(b, 2), "Power law fit test failed"

if __name__ == "__main__":
    test_jacobi()
    test_gauss_seidel()
    test_linear_regression()
    test_polynomial_regression()
    test_power_law_fit()
    print("All tests passed!")