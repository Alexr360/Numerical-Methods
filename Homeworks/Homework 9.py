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

def interpolate(x_query, data_points):
    x = [point[0] for point in data_points]
    y = [point[1] for point in data_points]

    xinterp = x_query
    yinterp = 0

    for i in range(len(x)):
        Li = 1
        for j in range(len(x)):
            if i != j:
                Li *= (xinterp - x[j]) / (x[i] - x[j])
        yinterp += Li * y[i]

    return yinterp

def ai_lagrange(x_query, data_pts):
    """
    AI-assisted version, created using Chat-GPT 04-mini-high: expects data_pts as list of (x, y) tuples.
    """
    result = 0.0
    n = len(data_pts)
    for i in range(n):
        xi, yi = data_pts[i]
        term = yi
        for j in range(n):
            if j != i:
                xj, _ = data_pts[j]
                term *= (x_query - xj) / (xi - xj)
        result += term
    return result

data = [(5,0.8), (10,1.6), (15,3.1), (20,4.5)]

theta_12_manual = interpolate(12, data)

theta_12_ai = ai_lagrange(12, data)

ans = [
    {'text': 'Final Answers', 'align': 'center', 'divider': True},
    {'text': f"In Class θ(12) | {theta_12_manual:.4f}°", 'align': 'center'},
    {'text': f"AI Gen θ(12)   | {theta_12_ai:.4f}°", 'align': 'center'}
]

ans_box(ans)