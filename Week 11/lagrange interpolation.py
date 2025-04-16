def lagrange_interpolation(x, x_values, y_values):
    """
    Perform Lagrange polynomial interpolation to estimate the value of y at a given x.
    
    Parameters:
    x (float): The x value to interpolate.
    x_values (list): List of known x values.
    y_values (list): List of known y values.
    
    Returns:
    float: The interpolated y value.
    """
    if len(x_values) != len(y_values):
        raise ValueError("x_values and y_values must have the same length.")
    
    n = len(x_values)
    if n < 2:
        raise ValueError("At least two data points are required for interpolation.")
    
    if x <= x_values[0]:
        return y_values[0]
    if x >= x_values[n-1]:
        return y_values[n-1]
    
    interpolated_y = 0.0
    for i in range(n):
        term = y_values[i]
        for j in range(n):
            if j != i:
                term *= (x - x_values[j]) / (x_values[i] - x_values[j])
        interpolated_y += term
    
    return interpolated_y