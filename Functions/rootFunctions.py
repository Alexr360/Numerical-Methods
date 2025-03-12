import numpy as np

def position_method(f, a, b, tol, iterations=0):
    # Check if the function has different signs at a and b
    if np.sign(f(a)) == np.sign(f(b)):
        raise Exception("The scalars a and b do not bound a root")

    m = a - f(a) * (b - a) / (f(b) - f(a))

    # Check if the absolute value of f(m) is less than the tolerance
    if np.abs(f(m)) < tol:
        return m, iterations

    # If f(a) and f(m) have different signs, recursively call position_method with m as the new a
    elif np.sign(f(a)) == np.sign(f(m)):
        return position_method(f, m, b, tol, iterations + 1)

    # If f(b) and f(m) have different signs, recursively call position_method with m as the new b
    elif np.sign(f(b)) == np.sign(f(m)):
        return position_method(f, a, m, tol, iterations + 1)

def bisection_method(f, a, b, tol, iterations=0):
    # Check if the function has different signs at a and b
    if np.sign(f(a)) == np.sign(f(b)):
        raise Exception("The scalars a and b do not bound a root")

    m = (a + b) / 2

    # Check if the absolute value of f(m) is less than the tolerance
    if np.abs(f(m)) < tol:
        return m, iterations

    # If f(a) and f(m) have different signs, recursively call bisection_method with m as the new a
    elif np.sign(f(a)) == np.sign(f(m)):
        return bisection_method(f, m, b, tol, iterations + 1)

    # If f(b) and f(m) have different signs, recursively call bisection_method with m as the new b
    elif np.sign(f(b)) == np.sign(f(m)):
        return bisection_method(f, a, m, tol, iterations + 1)
