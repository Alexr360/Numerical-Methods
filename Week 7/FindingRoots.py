import numpy as np

import matplotlib.pyplot as plt

def f(x):
    return np.cosh(x) * np.cos(x) + 1

def bisection_method(a, b, tol):
    if f(a) * f(b) >= 0:
        print("No root found in the given interval.")
        return None

    while (b - a) / 2 > tol:
        c = (a + b) / 2
        if f(c) == 0:
            return c
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c

    return (a + b) / 2

x = np.linspace(-10, 10, 1000)
y = f(x)

plt.plot(x, y)
plt.axhline(0, color='r', linestyle='--')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Graph of f(x) = cosh(x)cos(x) + 1')
plt.grid(True)
plt.show()

root = bisection_method(-10, 10, 1e-6)
if root is not None:
    print("Root:", root)