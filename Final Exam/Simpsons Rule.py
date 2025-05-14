import math

def simpson(f, a, b, n):
    """
    Approximate the integral of f(x) from a to b using Simpson's rule.
    
    Parameters:
        f : function
            The integrand, a function of one variable.
        a, b : float
            The lower and upper limits of integration.
        n : int
            Number of subintervals (must be even).
    
    Returns:
        float
            Approximation of the integral.
    """
    if n % 2:
        raise ValueError("Number of intervals n must be even.")
    
    h = (b - a) / n
    x0 = f(a) + f(b)
    
    # Sum of f at odd and even points
    odd_sum = 0.0
    even_sum = 0.0
    for i in range(1, n):
        x = a + i * h
        if i % 2 == 0:
            even_sum += f(x)
        else:
            odd_sum += f(x)
    
    return (h / 3) * (x0 + 4 * odd_sum + 2 * even_sum)

# Example usage:
if __name__ == "__main__":
    # Define the function to integrate, e.g., sin(x)
    def f(x):
        return math.sin(x)

    a = 0.0      # lower limit
    b = math.pi  # upper limit
    n = 100      # must be even

    result = simpson(f, a, b, n)
    print(f"Approximate integral of sin(x) from {a} to {b} with n={n}: {result:.6f}")
    # Expected value is 2.0
