import sys
import os
import numpy as np
from Functions.rootFunctions import *

# Define the function f(x) = cosh(x) * cos(x) + 1
f = lambda x: np.cosh(x) * np.cos(x) + 1

# Use the bisection method to find the root of f(x) in the interval [0, 2] with a tolerance of 0.01
bisection_ans, bisection_iterations = bisection_method(f, 0, 2, 1e-5)

# Use the roots method to find the root of f(x) in the interval [0, 2] with a tolerance of 0.01
position_ans, position_iterations = position_method(f, 0, 2, 1e-5)

# Calculate the similarity between the two roots as a percentage
difference = 100 - (abs(bisection_ans - position_ans) / bisection_ans * 100)

# Format strings dynamically
bisection_str = f"Bisection  Method     │ {bisection_ans} after {bisection_iterations} iterations"
position_str = f"False Position Method │ {position_ans} after {position_iterations} iterations"
accuracy_str = f"Accuracy: {difference:.2f}%"

# Determine the maximum content width
content_width = max(len(bisection_str), len(position_str), len(accuracy_str))

# Generate box borders dynamically
horizontal_border = "─" * (content_width + 2)
top_border = f"┌{horizontal_border}┐"
bottom_border = f"└{horizontal_border}┘"
divider = f"├{horizontal_border}┤"

# Print dynamically resized box
print(top_border)
print(f"│ Roots Calculated:{' ' * (content_width - len(' Roots Calculated:'))}  │")
print(divider)
print(f"│ {bisection_str}{' ' * (content_width - len(bisection_str))} │")
print(f"│ {position_str}{' ' * (content_width - len(position_str))} │")
print(divider)
print(f"│ {accuracy_str}{' ' * (content_width - len(accuracy_str))} │")
print(bottom_border)
