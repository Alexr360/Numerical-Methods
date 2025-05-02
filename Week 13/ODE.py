import numpy as np
import matplotlib.pyplot as plt

def f(t, y):
    return -2 * y

def euler_method(f, y0, t0, t_end, h):
    t = t0
    y = y0
    t_vals = [t]
    y_vals = [y]
    while t < t_end:
        y = y + h * f(t, y)
        t += h
        t_vals.append(t)
        y_vals.append(y)
    return np.array(t_vals), np.array(y_vals)

def heun_method(f, y0, t0, t_end, h):
    t = t0
    y = y0
    t_vals = [t]
    y_vals = [y]
    while t < t_end:
        k1 = f(t, y)
        y_pred = y + h * k1
        k2 = f(t + h, y_pred)
        y = y + (h/2) * (k1 + k2)
        t += h
        t_vals.append(t)
        y_vals.append(y)
    return np.array(t_vals), np.array(y_vals)

def rk4_method(f, y0, t0, t_end, h):
    t = t0
    y = y0
    t_vals = [t]
    y_vals = [y]
    while t < t_end:
        k1 = f(t, y)
        k2 = f(t + 0.5*h, y + 0.5*h*k1)
        k3 = f(t + 0.5*h, y + 0.5*h*k2)
        k4 = f(t + h, y + h*k3)
        y = y + (h/6)*(k1 + 2*k2 + 2*k3 + k4)
        t += h
        t_vals.append(t)
        y_vals.append(y)
    return np.array(t_vals), np.array(y_vals)

# Parameters
y0 = 1
t0 = 0
t_end = 5
h = 0.1   # try h=0.05 or 0.01 for even better accuracy

# Compute solutions
t_e, y_e = euler_method(f, y0, t0, t_end, h)
t_h, y_h = heun_method(f, y0, t0, t_end, h)
t_r, y_r = rk4_method(f, y0, t0, t_end, h)

# Exact solution
t_exact = np.linspace(t0, t_end, 500)
y_exact = np.exp(-2*t_exact)

# Plot
plt.figure(figsize=(8,5))
plt.plot(t_exact, y_exact, 'k-',   label='Exact $e^{-2t}$')
plt.plot(t_e,     y_e,     'b.-', label=f'Euler (h={h})')
plt.plot(t_h,     y_h,     'g.-', label=f'Heun (h={h})')
plt.plot(t_r,     y_r,     'r.-', label=f'RK4  (h={h})')
plt.title("Comparing Integrators for $\dot y=-2y$")
plt.xlabel('t')
plt.ylabel('y(t)')
plt.legend()
plt.grid(True)
plt.show()
