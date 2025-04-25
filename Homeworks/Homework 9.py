import numpy as np
import matplotlib.pyplot as plt

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

# Data
data = [(5,0.8), (10,1.6), (15,3.1), (20,4.5)]

# Compute θ(12)
theta_12_manual = interpolate(12, data)
print(f"In Class θ(12) = {theta_12_manual:.4f}°")

# Prepare data and compute
theta_12_ai = ai_lagrange(12, data)
print(f"AI Gen θ(12)   = {theta_12_ai:.4f}°")

