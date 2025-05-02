def euler_method(f, x0, y0, h, n):
    """
    Uses Euler's method to solve an ODE.

    Parameters:
    - f: The function representing the ODE dy/dx.
    - x0: The initial x value.
    - y0: The initial y value.
    - h: The step size.
    - n: The number of steps to take.

    Returns:
    - x: A list of x values.
    - y: A list of corresponding y values.
    """
    x = [x0]
    y = [y0]

    for i in range(n):
        x_i = x[i]
        y_i = y[i]
        y_i_plus_1 = y_i + h * f(x_i, y_i)
        x.append(x_i + h)
        y.append(y_i_plus_1)

    return x, y