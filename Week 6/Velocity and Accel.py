import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 5, 100)

x = 5*t**3 - 2*t**3 + 3*t - 7


v = np.gradient(x, t)
a = np.gradient(v, t)

plt.figure(figsize=(0, 5))
plt.plot(t, x, label='Position x(t)', linestyle='--', color='b')
plt.plot(t, v, label='Velocity v(t)', linestyle='-', color='r')
plt.plot(t, a, label='Acceleration a(t)', linestyle='-.', color='g')

plt.xlabel('Time (s)')
plt.ylabel('Magnitude')
plt.title('Position, Velocity, and Acceleration')
plt.legend()
plt.grid()
plt.show()