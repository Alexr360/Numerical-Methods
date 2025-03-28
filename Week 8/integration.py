import math
import numpy as np

import matplotlib.pyplot as plt

f = lambda x: np.exp(-x/4)*(2-x)-1
g = lambda x: 1/math.sqrt(1+x)

def fixedPointIteration(x0, e, N):
    step = 1
    flag = 1
    condition = True
    x_values = [x0]  # Store x values for plotting
    y_values = [f(x0)]  # Store f(x) values for plotting

    while condition:
        x1 = g(x0)
        x0 = x1
        step = step + 1
        if step > N:
            flag=0
            break
        condition = abs(f(x1)) > e

        x_values.append(x1)
        y_values.append(f(x1))

        # Plot the graph
        plt.plot(x_values, y_values, 'bo-')

    if flag==1:
        print('\nRequired root is: %0.8f' % x1)
    else:
        print('\nNot Convergent.\Last root is: %0.8f' % x1)

x0 = float(input('Enter Guess: '))
e = float(input('Tolerable Error: '))
N = int(input('Maximum Step: '))

fixedPointIteration(x0,e,N)

plt.xlabel('Iteration')
plt.ylabel('f(x)')
plt.title('Iteration vs. f(x)')
plt.grid(True)
plt.show()
