import numpy as np

import matplotlib.pyplot as plt

# Define the x and y data points
x = np.array([10, 15, 20, 25, 30, 35])
y = np.array([2.2, 4.6, 4.2, 7, 6.6, 9.2])

# Perform least square regression
coefficients = np.polyfit(x, y, 1)  # Fit a polynomial of degree 1 to the data
regression_line = np.poly1d(coefficients)  # Create a polynomial function using the coefficients

# Plot the data points and the regression line
plt.plot(x, y, 'o', label='Data')  # Plot the data points as circles
plt.plot(x, regression_line(x), label='Regression Line')  # Plot the regression line
plt.xlabel('x')  # Set the x-axis label
plt.ylabel('y')  # Set the y-axis label
plt.title('Plot of x vs y')  # Set the title of the plot
plt.grid(True)  # Show grid lines
plt.legend()  # Show the legend
plt.show()  # Display the plot
