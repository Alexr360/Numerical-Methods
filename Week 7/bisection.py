import numpy as np

import matplotlib.pyplot as plt

def bisection_method(f, a, b, tol, iterations=0):
    plt.legend()
    # Check if the function has different signs at a and b
    if np.sign(f(a)) == np.sign(f(b)):
        raise Exception("The scalars a and b do not bound a root")

    m = (a + b) / 2

    # Check if the absolute value of f(m) is less than the tolerance
    if np.abs(f(m)) < tol:
        plt.plot(m, f(m), 'o', color="Red", label=f'Final Root')  # Plot the current root with inverse autumn color
        plt.pause(0.1)  # Pause to show the plot
        plt.legend()
        return m, iterations

    # If f(a) and f(m) have different signs, recursively call bisection_method with m as the new a
    elif np.sign(f(a)) == np.sign(f(m)):
        print(f"Iteration {iterations}: {m}")
        color = plt.colormaps.get_cmap('autumn_r')(iterations / 20)  # Get inverse autumn color based on iteration
        plt.plot(m, f(m), 'o', color=color, label=f'Guess {iterations}')  # Plot the current root with inverse autumn color
        plt.pause(0.1)  # Pause to show the plot
        return bisection_method(f, m, b, tol, iterations + 1)

    # If f(b) and f(m) have different signs, recursively call bisection_method with m as the new b
    elif np.sign(f(b)) == np.sign(f(m)):
        print(f"Iteration {iterations}: {m}")
        color = plt.colormaps.get_cmap('autumn_r')(iterations / 20)  # Get inverse autumn color based on iteration
        plt.plot(m, f(m), 'o', color=color, label=f'Guess {iterations}')  # Plot the current root with inverse autumn color
        plt.pause(0.1)  # Pause to show the plot
        return bisection_method(f, a, m, tol, iterations + 1)

# Define the function f(x) = cosh(x) * cos(x) + 1
f = lambda x: np.cosh(x) * np.cos(x) + 1

# Plot the function f(x)
x = np.linspace(0, 2, 100)
plt.plot(x, f(x), label='f(x)')
plt.axhline(0, color='r', linestyle='--')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True)

# Use the bisection method to find the root of f(x) in the interval [0, 2] with a tolerance of 0.01
ans, iterations = bisection_method(f, 0, 2, 1e-5)

plt.title(f"Root at (~{ans:.3f}) after {iterations} iterations.")  # Add title with root coordinates
print(f"The root is {ans} after {iterations} iterations.")
plt.show()
