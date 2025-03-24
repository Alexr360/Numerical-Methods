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

def newton_raphson_method(func, dfunc, x0, tol=1.0e-6, max_iter=100):
    x = x0
    for i in range(max_iter):
        fx = func(x)
        dfx = dfunc(x)
        if dfx == 0:
            raise ValueError("Derivative is zero. No solution found.")
        x_new = x - fx / dfx
        if abs(x_new - x) < tol:
            return x_new, i + 1
        x = x_new
    raise ValueError("Maximum number of iterations reached")