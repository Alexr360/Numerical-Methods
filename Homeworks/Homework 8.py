import numpy as np
import matplotlib.pyplot as plt

# Given data
strain = np.array([0.000, 0.001, 0.002, 0.003, 0.004, 0.005, 0.006, 0.007])
stress = np.array([0.00, 85.1, 158.3, 223.4, 280.2, 328.7, 389.0, 401.0])

# Construct the design matrix for cubic regression
A = np.vstack([np.ones_like(strain), strain, strain**2, strain**3]).T

# Solve the normal equations: (A^T A) x = A^T b
coefficients = np.linalg.solve(A.T @ A, A.T @ stress)

# Generate the fitted curve
strain_fit = np.linspace(0, 0.007, 100)
stress_fit = coefficients[0] + coefficients[1] * strain_fit + coefficients[2] * strain_fit**2 + coefficients[3] * strain_fit**3

# Plot the original data and fitted curve
plt.scatter(strain, stress, color='red', label='Original Data')
plt.plot(strain_fit, stress_fit, color='blue', label='Cubic Fit')
plt.xlabel('Strain')
plt.ylabel('Stress (MPa)')
plt.title('Cubic Fit of Stress-Strain Data')
plt.legend()
plt.grid()
plt.show()
