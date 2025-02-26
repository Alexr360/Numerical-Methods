import numpy as np

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

# Create a single plot
plt.figure(figsize=(8, 5))
plt.xlabel('Radial Position (m)')
plt.ylabel('Velocity (m/s)')
plt.title('Velocity Profile in a Laminar Pipe Flow (Hagen-Poiseuille)')
plt.grid()

# Plot for each set of inputs
for input_values in input_values_list:
    r, u = plot_laminar_pipe_flow(*input_values)
    plt.plot(r, u, label=f'delta_p={input_values[0]}, mu={input_values[1]}, L={input_values[2]}, R={input_values[3]}')

plt.legend()
plt.show()