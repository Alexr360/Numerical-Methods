import numpy as np

import matplotlib.pyplot as plt

def interpolate(x_query, data_points):
    x = [point[0] for point in data_points]
    y = [point[1] for point in data_points]

    xinterp = np.linspace(x[0], x[-1], 100)  # Interpolation points
    yinterp = 0

    for i in range(len(x)):
        Li = 1
        for j in range(len(x)):
            if i != j:
                Li *= (xinterp - x[j]) / (x[i] - x[j])
        yinterp += Li * y[i]

    plt.plot(x, y, 'o-', label='Data Points')
    plt.plot(xinterp, yinterp, 'r-', label='Interpolated Point')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.show()

# Example usage
x_query = 3.5
data_points = [(1, 2), (2, 4), (4, 8), (5, 10)]
interpolate(x_query, data_points)