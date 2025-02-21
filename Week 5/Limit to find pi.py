import matplotlib.pyplot as plt
import numpy as np
import math

sum = 0
arr = [0]
for n in range(10):
    sum += (-1)**n /(3**n*(2*n+1))

    arr.append((2 * math.sqrt(3) * sum))

plt.plot(arr)
plt.xlabel('n')
plt.ylabel('PI')
plt.title('Plot of PI')
plt.show()