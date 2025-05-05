import numpy as np

import matplotlib.pyplot as plt

def f(t, y):
    """Right-hand side of the ODE dy/dt = 6 t^2 - 10 t + 3."""
    return 6 * t**2 - 10 * t + 3

def modified_eulers_method(f, x0, y0, h, n):
    """
    Solves an ODE using modified Euler's method.

    Parameters:
        f: Function representing dy/dt = f(t, y)
        x0: Initial value of x
        y0: Initial value of y
        h: Step size
        n: Number of steps

    Returns:
        t_values: List of time values
        y_values: List of y values
    """
    t_values = [x0]
    y_values = [y0]
    t, x, y = x0, x0, y0

    for i in range(n):
        k1 = h * f(t, y)
        k2 = h * f(t + h, y + k1)
        y = y + 0.5 * (k1 + k2)
        t = t + h
        t_values.append(t)
        y_values.append(y)

    return t_values, y_values


# Initial conditions
y0 = 1
t0 = 0
t_end = 5
h = 0.001
n = int((t_end - t0) / h)

# Solve the ODE using modified Euler's method
t_values, y_values = modified_eulers_method(f, t0, y0, h, n)

# Print results
for t, y in zip(t_values, y_values):
    print(f"t = {t:.2f}, y = {y:.6f}")

# Compute exact solution y = 2 t^3 - 5 t^2 + 3 t + 1
t_array = np.array(t_values)
y_exact = 2 * t_array**3 - 5 * t_array**2 + 3 * t_array + 1

# Plotting the results
plt.plot(t_values, y_values, 'b-', label='Modified Euler Approximation')
plt.plot(t_values, y_exact, 'k--', label='Exact Solution $2t^3 -5t^2 +3t +1$')
plt.title("Modified Euler's Method vs. Exact Solution for dy/dt = $6t^2 - 10t + 3$")
plt.xlabel('Time (t)')
plt.ylabel('y(t)')
plt.legend()
plt.grid(True)
plt.show()
