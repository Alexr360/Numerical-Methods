import math
import numpy as np

import matplotlib.pyplot as plt

def f(x):
    return np.exp(-x/4)*(2-x)-1

def g(x):
    return 1/math.sqrt(1+x)

def fixedPointIteration(initial_guess, tolerance, max_steps):
    x_values = [initial_guess]
    y_values = [f(initial_guess)]

    for step in range(1, max_steps + 1):
        x = g(x_values[-1])
        x_values.append(x)
        y_values.append(f(x))

    if abs(f(x)) <= tolerance:
        print(f'Required root is: {x:.8f}')
    else:
        print(f'Not Convergent. Last root is: {x:.8f}')

    return x_values, y_values

initial_guess = float(input('Enter Guess: '))
tolerance = float(input('Tolerable Error: '))
max_steps = int(input('Maximum Step: '))

x_values, y_values = fixedPointIteration(initial_guess, tolerance, max_steps)

plt.plot(x_values, y_values, 'bo-')
plt.xlabel('Iteration')
plt.ylabel('f(x)')
plt.title('Iteration vs. f(x)')
plt.grid(True)
plt.show()
