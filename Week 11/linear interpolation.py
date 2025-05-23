def linear_interpolation(x, x_values, y_values):
    """
    Perform linear interpolation to estimate the value of y at a given x.
    
    Parameters:
    x (float): The x value to interpolate.
    x_values (list): List of known x values.
    y_values (list): List of known y values.
    
    Returns:
    float: The interpolated y value.
    """
    # Check if x_values and y_values have the same length
    if len(x_values) != len(y_values):
        raise ValueError("x_values and y_values must have the same length.")
    
    n = len(x_values)
    
    # Check if at least two data points are available for interpolation
    if n < 2:
        raise ValueError("At least two data points are required for interpolation.")
    
    # Check if x is outside the range of x_values
    if x <= x_values[0]:
        return y_values[0]
    if x >= x_values[n-1]:
        return y_values[n-1]
    
    # Perform linear interpolation
    for i in range(1, n):
        if x <= x_values[i]:
            t = (x - x_values[i-1]) / (x_values[i] - x_values[i-1])
            return y_values[i-1] + t * (y_values[i] - y_values[i-1])