import numpy as np

def euler(f, x0, y0, h, n_steps):
    """
    Approximate solution of y' = f(x, y) using Euler's method.

    Parameters:
    - f: function f(x, y) defining the ODE
    - x0: initial x value
    - y0: initial y value
    - h: step size
    - n_steps: number of steps to take

    Returns:
    - xs: list of x values
    - ys: list of y values
    """
    xs = [x0]
    ys = [y0]
    x, y = x0, y0

    for i in range(n_steps):
        y = y + h * f(x, y)   # Euler update
        x = x + h
        xs.append(x)
        ys.append(y)

    return xs, ys


# Example usage:
if __name__ == "__main__":
    # Define the ODE: dy/dx = -2 * x * y
    def f(x, y):
        return -2 * x * y

    # Define the exact solution for comparison: y = exp(-x^2)
    def exact_solution(x):
        return np.exp(-x**2)

    # Initial condition y(0) = 1
    x0, y0 = 0.0, 1.0
    h = 0.1        # step size
    n = 50         # number of steps

    xs, ys = euler(f, x0, y0, h, n)

    # Generate exact solution values
    xs_exact = np.linspace(x0, x0 + n * h, 1000)
    ys_exact = exact_solution(xs_exact)

    import matplotlib.pyplot as plt

    # Plot the results
    plt.plot(xs, ys, label="Euler's Method", marker='o', linestyle='--')
    plt.plot(xs_exact, ys_exact, label="Exact Solution", color='red')
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Approximation using Euler's Method vs Exact Solution")
    plt.legend()
    plt.grid(True)
    plt.show()
