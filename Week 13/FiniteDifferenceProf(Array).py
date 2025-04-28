import numpy as np

import matplotlib.pyplot as plt

# Define the function f(x)
def f(x):
    return 2*x**3 - 5*x**2 + 3*x + 1

a = 0
b = 2
n = 50

x = np.linspace(a, b, n)
y = f(x)  # Add this line to calculate y values

h = (b - a) / n

# Calculate the exact differential
exact_diff = 6*x**2 - 10*x + 3

# Calculate forward difference approximation
forward_diff = (y[1:] - y[:-1]) / h

# Calculate backward difference approximation
backward_diff = (y[1:] - y[:-1]) / h

# Calculate central difference approximation
central_diff = (y[2:] - y[:-2]) / (2 * h)

# Print the difference approximations
print("Forward Difference: ", forward_diff)
print("Backward Difference: ", backward_diff)
print("Central Difference: ", central_diff)

# Plot the functions and approximations
plt.plot(x, y, label='f(x)')
plt.plot(x[:-1], forward_diff, label='Forward Difference')
plt.plot(x[:-1], backward_diff, label='Backward Difference')
plt.plot(x[1:-1], central_diff, label='Central Difference')
plt.plot(x, exact_diff, label='Exact Differential')
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.title('Finite Difference Approximations')
plt.show()
