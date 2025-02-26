import numpy as np
import matplotlib.pyplot as plt

def plot_laminar_pipe_flow(delta_p, mu, L, R):

    r = np.linspace(0, R, 100)

    u = (delta_p/(4*mu*L)) * (R**2 - r**2)

    plt.figure(figsize=(8,5))
    plt.plot(r, u, label='Velocity Profile', color='#ff00d4')
    plt.xlabel('Radial Position (m)')
    plt.ylabel('Velocity (m/s)')
    plt.title('Velocity Profile in a Laminar Pipe Flow (Hagen-Poiseuille)')
    plt.legend()
    plt.grid()
    plt.show()

plot_laminar_pipe_flow(500, 0.001, 1.0, 0.05)