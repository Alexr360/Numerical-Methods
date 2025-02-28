import numpy as np

import matplotlib.pyplot as plt

def plot_position_velocity_acceleration():
    """
    Plot the position, velocity, and acceleration over time.
    """
    t = np.linspace(0, 5, 50)

    # Calculate position, velocity, and acceleration
    x = 5*t**3 - 2*t**3 + 3*t - 7
    vr = 15*t**2 - 6*t**2 + 3
    ar = 30*t - 12*t

    v = np.gradient(x, t, edge_order=2)
    a = np.gradient(v, t, edge_order=2)

    # Plot the position, velocity, and acceleration
    plt.figure(figsize=(6, 5))
    plt.plot(t, x, label='Position x(t)', linestyle='-', color='b')
    plt.plot(t, vr, label='Velocity v(t) (real)', linestyle='-', color='r')
    plt.plot(t, ar, label='Acceleration a(t) (real)', linestyle='-', color='g')
    
    plt.plot(t, v, 'o', label='Velocity v(t)', color='r', fillstyle='none', markersize=4, alpha=0.5)
    plt.plot(t, a, 'o', label='Acceleration a(t)', color='g', fillstyle='none', markersize=4, alpha=0.5)

    plt.xlabel('Time (s)')
    plt.ylabel('Magnitude')
    plt.title('Position, Velocity, and Acceleration')
    plt.legend()
    plt.grid()
    plt.show()

# Call the function to plot the position, velocity, and acceleration
plot_position_velocity_acceleration()
