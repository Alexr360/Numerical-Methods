import numpy as np

def bisection_method(f, a, b, tol): 
    # Check if the function has different signs at a and b
    if np.sign(f(a)) == np.sign(f(b)):
        raise Exception("The scalars a and b do not bound a root")
        
    m = (a + b)/2
    
    # Check if the absolute value of f(m) is less than the tolerance
    if np.abs(f(m)) < tol:
        return m
    # If f(a) and f(m) have different signs, recursively call bisection_method with m as the new a
    elif np.sign(f(a)) == np.sign(f(m)):
        print(m)
        return bisection_method(f, m, b, tol)
    # If f(b) and f(m) have different signs, recursively call bisection_method with m as the new b
    elif np.sign(f(b)) == np.sign(f(m)):
        print(m)
        return bisection_method(f, a, m, tol)

# Define the function f(x) = x^2 - 2
f = lambda x: np.cosh(x) * np.cos(x) + 1

# Use the bisection method to find the root of f(x) in the interval [0, 2] with a tolerance of 0.01
ans = bisection_method(f, 0, 2, 1e-5)

# Print the result
print(ans)