import numpy as np

import matplotlib.pyplot as plt

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
        print(f"Iteration {iterations}: {m}")
        return bisection_method(f, m, b, tol, iterations + 1)

    # If f(b) and f(m) have different signs, recursively call bisection_method with m as the new b
    elif np.sign(f(b)) == np.sign(f(m)):
        print(f"Iteration {iterations}: {m}")
        return bisection_method(f, a, m, tol, iterations + 1)

# Define the function f(x) = x^2 - 2
f = lambda x: np.cosh(x) * np.cos(x) + 1

# Use the bisection method to find the root of f(x) in the interval [0, 2] with a tolerance of 0.01
ans, iterations = bisection_method(f, 0, 2, 1e-5)

# Plot the function and the points
x = np.linspace(0, 2, 100)
y = f(x)

plt.plot(x, y, label='f(x)')
plt.plot(ans, f(ans), 'ro', label='Root')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True)
plt.show()

# Print the result
print(f"The root is {ans} after {iterations} iterations.")