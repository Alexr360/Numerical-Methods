import numpy as np
import matplotlib.pyplot as plt

def f(t, y):
    """Right-hand side of the ODE dy/dt = 6 t^2 - 10 t + 3."""
    return 6 * t**2 - 10 * t + 3

def euler_method(f, y0, t0, t_end, h):
    """
    Solves an ODE using Euler's method.

    Parameters:
        f: Function representing dy/dt = f(t, y)
        y0: Initial value of y
        t0: Initial time
        t_end: End time
        h: Step size

    Returns:
        t_values: List of time values
        y_values: List of y values
    """
    t_values = [t0]
    y_values = [y0]
    t, y = t0, y0

    while t < t_end:
        y = y + h * f(t, y)
        t = t + h
        t_values.append(t)
        y_values.append(y)

    return t_values, y_values

# Initial conditions
y0 = 1
t0 = 0
t_end = 5
h = 0.1

# Solve the ODE
t_values, y_values = euler_method(f, y0, t0, t_end, h)

# Print results
for t, y in zip(t_values, y_values):
    print(f"t = {t:.2f}, y = {y:.6f}")

# Compute exact solution y = 2 t^3 - 5 t^2 + 3 t + 1
t_array = np.array(t_values)
y_exact = 2 * t_array**3 - 5 * t_array**2 + 3 * t_array + 1

# Plotting the results
plt.plot(t_values, y_values, 'b-', label='Euler Approximation')
plt.plot(t_values, y_exact, 'k--', label='Exact Solution $2t^3 -5t^2 +3t +1$')
plt.title("Euler's Method vs. Exact Solution for dy/dt = $6t^2 - 10t + 3$")
plt.xlabel('Time (t)')
plt.ylabel('y(t)')
plt.legend()
plt.grid(True)
plt.show()
