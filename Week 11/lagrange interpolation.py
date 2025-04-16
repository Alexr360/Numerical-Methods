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
    # Check if the lengths of x_values and y_values are the same
    if len(x_values) != len(y_values):
        raise ValueError("x_values and y_values must have the same length.")
    
    n = len(x_values)
    # Check if at least two data points are available for interpolation
    if n < 2:
        raise ValueError("At least two data points are required for interpolation.")
    
    # If x is less than or equal to the first x value, return the corresponding y value
    if x <= x_values[0]:
        return y_values[0]
    # If x is greater than or equal to the last x value, return the corresponding y value
    if x >= x_values[n-1]:
        return y_values[n-1]
    
    interpolated_y = 0.0
    for i in range(n):
        term = y_values[i]
        for j in range(n):
            if j != i:
                # Calculate the Lagrange polynomial term for each data point
                term *= (x - x_values[j]) / (x_values[i] - x_values[j])
        # Sum up all the terms to get the interpolated y value
        interpolated_y += term
    
    return interpolated_y