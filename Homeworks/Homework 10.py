import numpy as np
import matplotlib.pyplot as plt

# Given parameters
L = 2.0  # Length of the beam in meters
n = 4  # Number of subintervals
a = 0  # Start of the interval
b = L  # End of the interval
h = (b - a) / n  # Step size

# Define the function F(x)
def F(x):
    return 100 * np.sin(np.pi * x / L)

# Generate x values for plotting
x_dense = np.linspace(a, b, 500)
f_dense = F(x_dense)

# x and f values at integration points
x_vals = np.linspace(a, b, n + 1)
f_vals = F(x_vals)

# Plotting
plt.figure(figsize=(10, 6))

# Actual function
plt.plot(x_dense, f_dense, label='F(x) = 100 sin(πx/L)', color='blue')

# Trapezoidal segments
for i in range(n):
    x_trap = [x_vals[i], x_vals[i + 1]]
    y_trap = [f_vals[i], f_vals[i + 1]]
    plt.fill_between(x_trap, y_trap, color='orange', alpha=0.3, step='pre', label=f'Trapezoid' if i == 0 else "")
    plt.plot(x_trap, y_trap, color='orange', linestyle='--', label=f'Trapezoid Line' if i == 0 else "")

# Simpson's rule: draw parabolic arcs between every two in  rvals
from scipy.interpolate import BarycentricInterpolator

for i in range(0, n, 2):
    x_simpson = x_vals[i:i+3]
    y_simpson = f_vals[i:i+3]
    if len(x_simpson) == 3:
        poly = BarycentricInterpolator(x_simpson, y_simpson)
        x_interp = np.linspace(x_simpson[0], x_simpson[-1], 100)
        plt.plot(x_interp, poly(x_interp), color='green', linestyle='-.', label=f'Simpson Arc' if i == 0 else "")

# Plot points
plt.plot(x_vals, f_vals, 'ko', label='Sample Points')


# Final plot details
plt.title('Force Distribution and Numerical Integration Approximations')
plt.xlabel('x (m)')
plt.ylabel('F(x) (N)')
plt.grid(True)
plt.legend()
plt.show()

