import numpy as np

import matplotlib.pyplot as plt

def finite_difference(func, x, h):
    """
    Calculates the finite difference of a function at a given point.
    
    Parameters:
    - func: The function to calculate the finite difference of.
    - x: The point at which to calculate the finite difference.
    - h: The step size for the finite difference calculation.
    
    Returns:
    - The finite difference of the function at the given point.
    """
    return (func(x + h) - func(x)) / h

def plot_finite_difference(func, x_range, h):
    """
    Plots the finite difference of a function over a given range.
    
    Parameters:
    - func: The function to calculate the finite difference of.
    - x_range: The range of x values to plot.
    - h: The step size for the finite difference calculation.
    """
    x = np.linspace(x_range[0], x_range[1], 100)
    y = [finite_difference(func, xi, h) for xi in x]
    
    plt.plot(x, y)
    plt.xlabel('x')
    plt.ylabel('Finite Difference')
    plt.title('Finite Difference of Function')
    plt.grid(True)
    plt.show()