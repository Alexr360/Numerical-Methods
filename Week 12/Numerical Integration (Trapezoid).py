import numpy as np

import matplotlib.pyplot as plt

# Define the function f(x)
def f(x):
    return 2*x**3 - 5*x**2 + 3*x + 1

# Generate x and y values for plotting
x = np.linspace(0, 2, 50)
y = f(x)

# Trapezoid Rule
def trapezoid_rule(f, a, b, n):
    h = (b - a) / n
    x = np.linspace(a, b, n+1)
    y = f(x)
    area = h * (np.sum(y) - 0.5 * (y[0] + y[-1]))
    return area

# Calculate and plot the trapezoid rule
n = 50  # Number of subintervals
area = trapezoid_rule(f, 0, 2, n)

print(area)

# Plot the function and the area under the curve
plt.plot(x, y)
plt.fill_between(x, y, where=(x >= 0) & (x <= 2), color='gray', alpha=0.5)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Plot of f(x) with Trapezoid Rule')
plt.grid(True)
plt.show()