import numpy as np

A = np.array([[1, 1], [2, 4]])  # Define matrix A
B = np.array([10, 28])  # Define vector

x = np.linalg.solve(A,B)
print(x)