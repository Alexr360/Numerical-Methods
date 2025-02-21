import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Create data
x = np.random.rand(100)
y = np.random.rand(100)
z = np.random.rand(100)

x1 = np.random.rand(100)
y1 = np.random.rand(100)
z1 = np.random.rand(100)

# Create figure and axes object
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the data
ax.scatter(x, y, z)
ax.scatter(x1, y1, z1)

# Set labels
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

# Set title
ax.set_title('3D Scatter Plot')

# Show the plot
plt.show()