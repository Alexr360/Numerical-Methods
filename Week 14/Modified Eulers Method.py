import numpy as np

import matplotlib.pyplot as plt

def f(t, y):
    """Right-hand side of the ODE dy/dt = 6 t^2 - 10 t + 3."""
    return 6 * t**2 - 10 * t + 3

def modified_eulers_method(f, x0, y0, h, n):
    """
    Solve an ordinary differential equation using the modified Euler's method.

    Parameters:
    f: function
        The function defining the ODE dy/dx = f(x, y).
    x0: float
        The initial x value.
    y0: float
        The initial y value.
    h: float
        The step size.
    n: int
        The number of steps to take.

    Returns:
    x: list
        The x values.
    y: list
        The corresponding y values.
    """
    x = [x0]
    y = [y0]

    for i in range(n):
        xi = x[i]
        yi = y[i]

        k1 = h * f(xi, yi)
        k2 = h * f(xi + h/2, yi + k1/2)

        xi1 = xi + h
        yi1 = yi + k2

        x.append(xi1)
        y.append(yi1)

    return x, y

# Initial conditions
y0 = 1
t0 = 0
t_end = 5
h = 0.001

# Solve the ODE using modified Euler's method
t_values, y_values = modified_eulers_method(f, t0, y0, h, int((t_end - t0) / h))

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
