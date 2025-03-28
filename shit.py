import numpy as np

A = np.array([[1, 1], [2, 4]])  # Define matrix A
B = np.array([10, 28])  # Define vector B
sol = np.zeros(len(B))  # Initialize solution vector

for k in range(10):  # Iterate 10 times
    for i in range(len(B)):  # Iterate over each element of B
        sum_temp = np.dot(A[i, :], sol[:]) - A[i, i] * B[i]  # Calculate the temporary sum
        sol[i] = (B[i] - sum_temp) / A[i, i]  # Update the solution for the current element
    print(k, sol)  # Print the iteration number and the current solution
