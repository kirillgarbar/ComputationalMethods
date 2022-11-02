from polynomial_value_at_point import polynomial_value_at_point
from Roots.reduce_roots import bisection_method
from Roots.separate_roots import separate_roots
from utils import f

def bisection_method_inverse_interpolation(a, b, accuracy, points, table, point):
    function = lambda x: polynomial_value_at_point(points, table, x) - point
    separated_values = separate_roots(function, a, b, 1000)
    roots = bisection_method(function, separated_values, accuracy)

    if len(roots) > 1:
        raise RuntimeError(
            f"More than one root was found."
            f"\nRoots: {roots}."
            f"\nValues at answers: {[function(answer) for answer in roots]}")
    answer = roots[0][0]

    print(f"Bisection reduced value at {point} is {answer}")
    print(
        f"Absolute value bisection method discrepancy: {abs(point - f(answer))}")
