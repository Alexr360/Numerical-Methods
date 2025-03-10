import numpy as np

import matplotlib.pyplot as plt

def position_method(f, a, b, tol, delta, iterations=0):
    plt.legend()
    # Check if the function has different signs at a and b
    if np.sign(f(a)) == np.sign(f(b)):
        raise Exception("The scalars a and b do not bound a root")

    m = a - f(a) * (b - a) / (f(b) - f(a))

    # Check if the absolute value of f(m) is less than the tolerance
    if np.abs(f(m)) < delta:
        plt.plot(m, f(m), 'x', color="Red", label=f'Final Root')  # Plot the current root with inverse autumn color
        plt.pause(0.1)  # Pause to show the plot
        plt.legend()
        return m, iterations

    # If f(a) and f(m) have different signs, recursively call position_method with m as the new a
    elif np.sign(f(a)) == np.sign(f(m)):
        print(f"Iteration {iterations}: {m}")
        color = plt.colormaps.get_cmap('autumn_r')(iterations / 20)  # Get inverse autumn color based on iteration
        plt.plot(m, f(m), 'o', color=color, label=f'Guess {iterations}')  # Plot the current root with inverse autumn color
        plt.pause(0.1)  # Pause to show the plot
        return position_method(f, m, b, tol, delta, iterations + 1)

    # If f(b) and f(m) have different signs, recursively call position_method with m as the new b
    elif np.sign(f(b)) == np.sign(f(m)):
        print(f"Iteration {iterations}: {m}")
        color = plt.colormaps.get_cmap('autumn_r')(iterations / 20)  # Get inverse autumn color based on iteration
        plt.plot(m, f(m), 'o', color=color, label=f'Guess {iterations}')  # Plot the current root with inverse autumn color
        plt.pause(0.1)  # Pause to show the plot
        return position_method(f, a, m, tol, delta, iterations + 1)

# Define the function f(x) = cosh(x) * cos(x) + 1
f = lambda x: np.cosh(x) * np.cos(x) + 1

# Plot the function f(x)
x = np.linspace(0, 2, 100)
# plt.figure(figsize=(8, 6)) #This line makes the last point not show up in the legend
plt.plot(x, f(x), label='f(x)')
plt.axhline(0, color='r', linestyle='--')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True)

# Use the position method to find the root of f(x) in the interval [0, 2] with a tolerance of 0.01 and a delta of 1e-5
ans, iterations = position_method(f, 0, 2, 0.01, 1e-5)

plt.title(f"Root at (~{ans:.3f}) after {iterations} iterations.")  # Add title with root coordinates
print(f"The root is {ans} after {iterations} iterations.")
plt.show()
