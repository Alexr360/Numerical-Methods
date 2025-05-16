def euler(f, x0, y0, h, n):
    """
    Approximate solution of y' = f(x, y) using Euler's method.

    Parameters:
    - f: function f(x, y) defining the ODE
    - x0: initial x value
    - y0: initial y value
    - h: step size
    - n: number of steps to take

    Returns:
    - xs: list of x values
    - ys: list of y values
    """
    xs = [x0]
    ys = [y0]
    x, y = x0, y0

    for _ in range(n):
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

    # Initial condition y(0) = 1
    x0, y0 = 0.0, 1.0
    h = 0.1        # step size
    n = 50         # number of steps

    xs, ys = euler(f, x0, y0, h, n)

    # Print the results
    for xi, yi in zip(xs, ys):
        print(f"x = {xi:.2f},    y ≈ {yi:.6f}")
