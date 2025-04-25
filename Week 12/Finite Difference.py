import numpy as np

import matplotlib.pyplot as plt

# Define the function f(x)
def f(x):
    """
    Returns the value of the function f(x) = 2x^3 - 5x^2 + 3x + 1.
    """
    return 2*x**3 - 5*x**2 + 3*x + 1

# Define the derivative of the function f'(x)
def f_prime(x):
    """
    Returns the value of the derivative of the function f'(x) = 6x^2 - 10x + 3.
    """
    return 6*x**2 - 10*x + 3

# Generate x and y values for plotting
x = np.linspace(0, 2, 50)
y = f(x)
y_prime = f_prime(x)

# Define forward and backward difference approximations
forward_difference = lambda x, h: (f(x + h) - f(x)) / h
backward_difference = lambda x, h: (f(x) - f(x - h)) / h

# Plot the function, its derivative, and finite difference approximations
plt.plot(x, y, label='f(x)')
plt.plot(x, y_prime, label="f'(x)")
plt.plot(x, forward_difference(x, 0.1), label='Forward Difference')
plt.plot(x, backward_difference(x, 0.1), label='Backward Difference')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
