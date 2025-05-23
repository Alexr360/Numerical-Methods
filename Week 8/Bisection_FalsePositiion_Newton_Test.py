import math
from Functions.RootFindingMethods import bisection_method, false_position_method, newton_raphson_method

def test_bisection_method():
    # Test case 1: Root of a quadratic function
    def func1(x):
        return x**2 - 4

    root = bisection_method(func1, 0, 3)
    assert abs(root - 2) < 1.0e-6, f"Expected root near 2, got {root}"

    # Test case 2: Root of a cubic function
    def func2(x):
        return x**3 - x - 2

    root = bisection_method(func2, 1, 2)
    assert abs(root - 1.5213797) < 1.0e-6, f"Expected root near 1.5213797, got {root}"

    # Test case 3: Root of a trigonometric function
    def func3(x):
        return math.cos(x) - x

    root = bisection_method(func3, 0, 1)
    assert abs(root - 0.7390851) < 1.0e-6, f"Expected root near 0.7390851, got {root}"

    print("All tests passed for Bisection method.")

def test_false_position_method():
    # Test case 1: Root of a quadratic function
    def func1(x):
        return x**2 - 4

    root = false_position_method(func1, 0, 3)
    assert abs(root - 2) < 1.0e-6, f"Expected root near 2, got {root}"

    # Test case 2: Root of a cubic function
    def func2(x):
        return x**3 - x - 2

    root = false_position_method(func2, 1, 2)
    assert abs(root - 1.5213797) < 1.0e-6, f"Expected root near 1.5213797, got {root}"

    # Test case 3: Root of a trigonometric function
    def func3(x):
        return math.cos(x) - x

    root = false_position_method(func3, 0, 1)
    assert abs(root - 0.7390851) < 1.0e-6, f"Expected root near 0.7390851, got {root}"

    # Test case 4: Function with no root in the interval
    def func4(x):
        return x**2 + 1

    try:
        false_position_method(func4, -1, 1)
    except ValueError as e:
        assert str(e) == "The function must have different signs at a and b", f"Unexpected error message: {e}"

    print("All tests passed for False Position method.")

def test_newton_raphson_method():
    # Test case 1: Root of a quadratic function
    def func1(x):
        return x**2 - 4

    root = newton_raphson_method(func1, 3)
    assert abs(root - 2) < 1.0e-6, f"Expected root near 2, got {root}"

    # Test case 2: Root of a cubic function
    def func2(x):
        return x**3 - x - 2

    root = newton_raphson_method(func2, 2)
    assert abs(root - 1.5213797) < 1.0e-6, f"Expected root near 1.5213797, got {root}"

    # Test case 3: Root of a trigonometric function
    def func3(x):
        return math.cos(x) - x

    root = newton_raphson_method(func3, 1)
    assert abs(root - 0.7390851) < 1.0e-6, f"Expected root near 0.7390851, got {root}"

    print("All tests passed for Newton-Raphson method.")


test_bisection_method()
test_false_position_method()
test_newton_raphson_method()