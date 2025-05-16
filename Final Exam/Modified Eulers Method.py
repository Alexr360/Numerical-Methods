def modified_euler(f, x, y, h, n):
    """
    Approximate solution of y' = f(x, y) using the modified (Heun's) Euler method.

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
    xs = [x]
    ys = [y]

    for _ in range(n):
        k1 = f(x, y)
        # predictor step (Euler)
        y_pred = y + h * k1
        x_next = x + h
        # corrector slope at the end of interval
        k2 = f(x_next, y_pred)
        # average slope
        y = y + (h / 2) * (k1 + k2)
        x = x_next

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

    xs, ys = modified_euler(f, x0, y0, h, n)

    # Print the results
    for xi, yi in zip(xs, ys):
        print(f"x = {xi:.2f},    y ≈ {yi:.6f}")
