import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

def plot_laminar_pipe_flow(delta_p, mu, L, R):
    r = np.linspace(0, R, 100)
    u = (delta_p / (4 * mu * L)) * (R ** 2 - r ** 2)
    return r, u

# List of input values
input_values_list = [
    [750, 0.001, 1.0, 0.05],
    [500, 0.001, 1.0, 0.05],
    [250, 0.001, 1.0, 0.05]
]

fig = plt.figure(figsize=(8, 5))
ax = fig.add_subplot(111, projection='3d')

for input_values in input_values_list:
    r, u = plot_laminar_pipe_flow(*input_values)
    R = input_values[3]
    ax.plot(r, [R] * len(r), u, label=f'delta_p={input_values[0]}, mu={input_values[1]}, L={input_values[2]}, R={input_values[3]}')

ax.set_xlabel('Radial Position (m)')
ax.set_ylabel('R (m)')
ax.set_zlabel('Velocity (m/s)')
ax.set_title('Velocity Profile in a Laminar Pipe Flow (Hagen-Poiseuille)')
ax.legend()

plt.show()
