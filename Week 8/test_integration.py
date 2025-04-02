def test_one_point_iteration():
    f = lambda x: x**2 - 4
    x0 = 2
    tol = 1e-6
    max_iter = 100
    result = one_point_iteration(f, x0, tol, max_iter)
    expected = 2.0

    assert abs(result - expected) < tol, "Test failed: Expected {}, but got {}".format(expected, result)

test_one_point_iteration()
