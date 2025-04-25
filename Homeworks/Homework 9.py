import numpy as np
import matplotlib.pyplot as plt

def ans_box(config):
    if not config or not isinstance(config, list):
        return
    
    # Extract content from config
    content = [line['text'] for line in config]
    
    # Calculate maximum content width
    content_width = max(len(line) for line in content)
    
    # Create dynamic borders
    horizontal_border = "─" * (content_width + 2)
    top_border = f"┌{horizontal_border}┐"
    bottom_border = f"└{horizontal_border}┘"
    divider = f"├{horizontal_border}┤"
    
    # Print the box
    print(top_border)
    for i, line in enumerate(config):
        text = line['text']
        align = line.get('align', 'left')
        
        # Handle alignment
        if align == 'center':
            padding_left = (content_width - len(text)) // 2
            padding_right = content_width - len(text) - padding_left
        elif align == 'right':
            padding_left = content_width - len(text)
            padding_right = 0
        else:
            padding_left = 0
            padding_right = content_width - len(text)
        
        # Print the line with padding
        print(f"│ {' ' * padding_left}{text}{' ' * padding_right} │")
        
        # Handle dividers based on config
        if line.get('divider', False):
            print(divider)
    print(bottom_border)

# Function to perform Lagrange interpolation
def interpolate(xinterp, data_points):
    x = [point[0] for point in data_points]
    y = [point[1] for point in data_points]
    yinterp = 0
    for i in range(len(x)):
        Li = 1
        for j in range(len(x)):
            if i != j:
                Li *= (xinterp - x[j]) / (x[i] - x[j])
        yinterp += Li * y[i]

    return yinterp

# Function to perform AI-assisted Lagrange interpolation
def lagrange_interpolation(x, y, x0):
    """
    Compute the Lagrange interpolation polynomial at x0
    given data points (x, y).
    """
    x = np.array(x)
    y = np.array(y)
    n = len(x)
    total = 0.0
    for i in range(n):
        term = y[i]
        for j in range(n):
            if j != i:
                term *= (x0 - x[j]) / (x[i] - x[j])
        total += term
    return total

# Data points for interpolation
T = [5, 10, 15, 20]              # Torque in N·m
theta = [0.8, 1.6, 3.1, 4.5]     # Angle of twist in degrees
data = [(5,0.8), (10,1.6), (15,3.1), (20,4.5)]

# Perform manual interpolation
ans_manual = interpolate(12, data)

# Perform AI-assisted interpolation
ans_ai = lagrange_interpolation(T, theta, 12)

# Calculate the difference
difference = (ans_manual - ans_ai) / ans_manual * 100

# Print the answers in a formatted box
ans_box([
    {'text': 'Final Answers', 'align': 'center', 'divider': True},
    {'text': f"In Class θ(12) | {ans_manual:.4f}°", 'align': 'center'},
    {'text': f"AI Gen θ(12)   | {ans_ai:.4f}°", 'align': 'center', 'divider': True},
    {'text': f"Percent Difference | {difference}", 'align': 'center'}
])