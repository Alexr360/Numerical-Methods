import numpy as np

import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 1000)
y = np.cosh(x) * np.cos(x) + 1

plt.plot(x, y)
plt.axhline(0, color='r', linestyle='--')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Graph of f(x) = cosh(x)cos(x) + 1')
plt.grid(True)
print("     ┌──────────────────────────┐\n     │ Close Figure to Continue │\n     └──────────────────────────┘")
plt.show()
roots = np.roots([1, 0, 1, 0, 1])  # Coefficients of the polynomial
print("Roots:", roots)