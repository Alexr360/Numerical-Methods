def lagrange_interpolate(x, x_pts, y_pts):
    """
    Compute Lagrange interpolation at x for data (x_pts, y_pts).
    """
    total = 0.0
    n = len(x_pts)
    for i in range(n):
        xi, yi = x_pts[i], y_pts[i]
        Li = 1.0
        for j in range(n):
            if j != i:
                Li *= (x - x_pts[j]) / (xi - x_pts[j])
        total += yi * Li
    return total

# Data
T = [5, 10, 15, 20]
theta = [0.8, 1.6, 3.1, 4.5]

# Compute θ(12)
theta_12_manual = lagrange_interpolate(12, T, theta)
print(f"Manual θ(12) = {theta_12_manual:.4f}°")

def ai_lagrange(x_query, data_pts):
    """
    AI-assisted version: expects data_pts as list of (x, y) tuples.
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

# Prepare data and compute
data = [(5,0.8), (10,1.6), (15,3.1), (20,4.5)]
theta_12_ai = ai_lagrange(12, data)
print(f"AI θ(12)     = {theta_12_ai:.4f}°")

