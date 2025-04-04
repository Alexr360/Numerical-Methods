import numpy as np
import matplotlib.pyplot as plt

def plot_regression():
    """
    Plot the data points and the regression line.
    """
    # Define the x and y data points
    x = np.array([10, 15, 20, 25, 30, 35])
    y = np.array([2.2, 4.6, 4.2, 7, 6.6, 9.2])

    # Calculate the regression line
    n = len(x)
    sum_x = np.sum(x)
    sum_x2 = np.sum(x**2)
    sum_y = np.sum(y)
    sum_xy = np.sum(x*y)

    A = np.array([[n, sum_x], [sum_x, sum_x2]])  # Fill out the matrix A
    B = np.array([sum_y, sum_xy])
    a = np.linalg.solve(A, B)

    # Plot the regression line and data points
    plt.plot(x, a[0] + a[1]*x, label='Regression Line')
    plt.plot(x, y, 'o', label='Data')
    plt.xlabel('x')  # Set the x-axis label
    plt.ylabel('y')  # Set the y-axis label
    plt.title('Plot of x vs y')  # Set the title of the plot
    plt.grid(True)  # Show grid lines
    plt.legend()  # Show the legend
    plt.show()

plot_regression()
