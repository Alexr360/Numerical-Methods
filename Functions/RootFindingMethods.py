import numpy as np

def bisection_method(func, a, b, tol=1.0e-6, max_iter=100):
    if func(a) * func(b) >= 0:
        raise ValueError("The function must have different signs at a and b")
    
    for _ in range(max_iter):
        c = (a + b) / 2.0
        if func(c) == 0 or (b - a) / 2.0 < tol:
            return c
        if func(c) * func(a) < 0:
            b = c
        else:
            a = c
    raise ValueError("Maximum number of iterations reached")

def false_position_method(func, a, b, tol=1.0e-6, max_iter=100):
    if func(a) * func(b) >= 0:
        raise ValueError("The function must have different signs at a and b")
    
    for _ in range(max_iter):
        c = b - (func(b) * (b - a)) / (func(b) - func(a))
        if func(c) == 0 or abs(func(c)) < tol:
            return c
        if func(c) * func(a) < 0:
            b = c
        else:
            a = c
    raise ValueError("Maximum number of iterations reached")

def newton_raphson_method(f, x0, tol=1e-6, max_iter=100, h=1e-5):
    """Newton-Raphson method with numerical differentiation using finite differences."""
    x = x0
    for _ in range(max_iter):
        fx = f(x)
        dfx = (f(x + h) - fx) / h  # Numerical derivative using finite difference
        
        if abs(dfx) < 1e-12:  # Avoid division by zero
            raise ValueError("Numerical derivative is too small; try a different initial guess or step size.")
        
        x_new = x - fx / dfx  # Newton-Raphson update step
        
        if abs(x_new - x) < tol:
            return x_new  # Convergence reached
        
        x = x_new  # Update estimate
    raise ValueError("Maximum number of iterations reached")