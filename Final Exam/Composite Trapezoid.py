import math

def composite_trapezoid(f, a, b, n):
    """
    Approximate the integral of f(x) from a to b using the composite trapezoid rule
    with n subintervals.
    
    Parameters:
        f : function
            The integrand, a function of one variable.
        a : float
            Lower limit of integration.
        b : float
            Upper limit of integration.
        n : int
            Number of equally spaced subintervals (n >= 1).
            
    Returns:
        float
            Approximation of the integral.
    """
    # Step size
    h = (b - a) / n
    
    # Evaluate endpoints
    total = 0.5 * (f(a) + f(b))
    
    # Sum interior points
    for i in range(1, n):
        x = a + i * h
        total += f(x)
    
    # Multiply by step size
    return total * h

# Example usage
if __name__ == "__main__":
    # Integrate sin(x) from 0 to pi
    result = composite_trapezoid(math.sin, 0, math.pi, 10000)
    print(f"Approximate integral of sin(x) from 0 to pi ≈ {result:.6f}")
    # True value is 2.0
