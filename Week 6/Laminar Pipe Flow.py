import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def plot_laminar_pipe_flow(delta_p, mu, L, R):
    r = np.linspace(0, R, 100)  # Radial positions
    θ = np.linspace(0, 2 * np.pi, 100)  # Angular positions
    R_mesh, Θ_mesh = np.meshgrid(r, θ)  # Create grid
    
    # Velocity field (Hagen-Poiseuille equation)
    U_mesh = (delta_p / (4 * mu * L)) * (R ** 2 - R_mesh ** 2)

    # Convert polar (r, θ) to Cartesian (x, y)
    X = R_mesh * np.cos(Θ_mesh)
    Y = R_mesh * np.sin(Θ_mesh)
    
    return X, Y, U_mesh

# List of input values with distinct ΔP values
input_values_list = [
    [750, 0.001, 1.0, 0.05],  # High pressure drop
    [500, 0.001, 1.0, 0.05],  # Medium pressure drop
    [250, 0.001, 1.0, 0.05]   # Low pressure drop
]

# Assign a different colormap to each dataset
colormaps = ['viridis', 'plasma', 'coolwarm']
colors = ['g', 'b', 'r']

fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# Plot distinct surfaces for each ΔP
for idx, input_values in enumerate(input_values_list):
    X, Y, U = plot_laminar_pipe_flow(*input_values)
    cmap = colormaps[idx]  # Choose a colormap
    color = colors[idx]  # Choose a color for the wireframe
    # ax.plot_surface(X, Y, U, cmap=cmap, alpha=0.7)  # Surface plot
    ax.plot_wireframe(X, Y, U, color=color, linewidth=0.4, alpha=0.4)  # Wireframe for contrast

ax.set_xlabel('X (m)')
ax.set_ylabel('Y (m)')
ax.set_zlabel('Velocity (m/s)')
ax.set_title('Laminar Pipe Flow Velocity Profile (Distinct Surfaces)')
plt.show()
