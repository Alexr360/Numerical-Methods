import numpy as np
import math

pi=0
for i in range(10):
    pi += ((-1)**i) / (3**i * (2*i+1))
    print(i, 2 * math.sqrt(3) * pi)

pi = 2 * math.sqrt(3) * pi

print(f"Series: {pi}\nReal: {math.pi}")