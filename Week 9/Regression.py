import numpy as np

import matplotlib.pyplot as plt

# Define the x and y data points
x = np.array([10, 15, 20, 25, 30, 35])
y = np.array([2.2, 4.6, 4.2, 7, 6.6, 9.2])

# Square the elements of x and y using list comprehension
x_squared = [xi**2 for xi in x]
y_squared = [yi**2 for yi in y]

# Perform linear regression
coefficients = np.polyfit(x_squared, y_squared, 1)  # Fit a polynomial of degree 1 to the squared data
regression_line = np.poly1d(coefficients)  # Create a polynomial function using the coefficients

# Plot the data points and the regression line
plt.plot(x_squared, y_squared, 'o', label='Data')  # Plot the squared data points as circles
plt.plot(x_squared, regression_line(x_squared), label='Regression Line')  # Plot the regression line
plt.xlabel('x^2')  # Set the x-axis label
plt.ylabel('y^2')  # Set the y-axis label
plt.title('Plot of x^2 vs y^2')  # Set the title of the plot
plt.grid(True)  # Show grid lines
plt.legend()  # Show the legend
plt.show()  # Display the plot