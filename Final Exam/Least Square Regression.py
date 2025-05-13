def linear_regression(x, y):
    n = len(x)
    if n != len(y):
        raise ValueError("x and y must have the same length")

    # Calculate means
    x_mean = sum(x) / n
    y_mean = sum(y) / n

    # Calculate numerator and denominator for the slope in one loop
    num, den = 0, 0
    for xi, yi in zip(x, y):
        num += (xi - x_mean) * (yi - y_mean)
        den += (xi - x_mean) ** 2

    if den == 0:
        raise ValueError("Variance of x is zero. Cannot compute slope.")

    m = num / den
    b = y_mean - m * x_mean

    return m, b


def predict(x, m, b):
    return m * x + b


# Example usage:
if __name__ == "__main__":
    # Sample data
    x_vals = [1, 2, 3, 4, 5]
    y_vals = [2, 4, 5, 4, 5]

    # Fit the line
    slope, intercept = linear_regression(x_vals, y_vals)
    print(f"Slope (m): {slope:.3f}")
    print(f"Intercept (b): {intercept:.3f}")

    # Make predictions
    y_pred = predict(3, slope, intercept)
    print(f"Predicted y values:{y_pred:.3f}")
