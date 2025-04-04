import numpy as np

import matplotlib.pyplot as plt

def plot_regression():
    """
    Plot the data points and the quadratic regression line.
    """
    # Define the x and y data points
    x = np.array([10, 15, 20, 25, 30, 35])
    y = np.array([2.2, 4.6, 4.2, 7, 6.6, 9.2])

    # Calculate the quadratic regression line
    n = len(x)
    sum_x = np.sum(x)
    sum_x2 = np.sum(x**2)
    sum_x3 = np.sum(x**3)
    sum_x4 = np.sum(x**4)
    sum_y = np.sum(y)
    sum_xy = np.sum(x*y)
    sum_x2y = np.sum(x**2*y)

    A = np.array([[n, sum_x, sum_x2], [sum_x, sum_x2, sum_x3], [sum_x2, sum_x3, sum_x4]])  # Fill out the matrix A
    B = np.array([sum_y, sum_xy, sum_x2y])
    a = np.linalg.solve(A, B)

    # Plot the quadratic regression line and data points
    x_range = np.linspace(min(x), max(x), 100)
    y_range = a[0] + a[1]*x_range + a[2]*x_range**2
    plt.plot(x_range, y_range, label='Quadratic Regression Line')
    plt.plot(x, y, 'o', label='Data')
    plt.xlabel('x')  # Set the x-axis label
    plt.ylabel('y')  # Set the y-axis label
    plt.title('Plot of x vs y')  # Set the title of the plot
    plt.grid(True)  # Show grid lines
    plt.legend()  # Show the legend
    plt.show()

plot_regression()
