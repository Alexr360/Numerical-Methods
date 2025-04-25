import numpy as np

import matplotlib.pyplot as plt

# Define the function f(x)
def f(x):
    return 2*x**3 - 5*x**2 + 3*x + 1

# Define the derivative of the function f'(x)
def f_prime(x):
    return 6*x**2 - 10*x + 3

# Generate x and y values for plotting
x = np.linspace(0, 2, 50)
y = f(x)
y_prime = f_prime(x)

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
