from sympy import lambdify, integrate, diff,  maximum, Interval, parse_expr
from sympy.abc import x


def print_result(name, value, error, theoretical, precise):
    print(f"\n{name}\n"
          f"Value: {value}; "
          f"Error: {error}; "
          f"Relative error: {error / abs(precise) * 100}; "
          f"Theoretical: {theoretical}")

def integrate_with_all_methods(a, b, m, f_expr):
    precise_integral = integrate(f_expr, (x, a, b))
    f = lambdify(x, f_expr, "numpy")
    h = (b - a) / m
    print(f'Left border: {a}\nRight border: {b}\nNumber of intervals: {m}\nStep size: {h}')
    print(f'Precise integral: {precise_integral}\n')

    w = 0
    for j in range(1, m):
        w += f(a + j * h)

    left_rectangles = h * (f(a) + w)
    right_rectangles = h * (f(b) + w)

    q = 0
    for j in range(m):
        q += f(a + j * h + (h / 2))

    middle_rectangles = h * q

    z = f(a) + f(b)

    trapezoid = (h / 2) * (z + 2 * w)
    simpson = (h / 6) * (z + 2 * w + 4 * q)

    left_discrepancy = abs(precise_integral - left_rectangles)
    right_discrepancy = abs(precise_integral - right_rectangles)
    middle_discrepancy = abs(precise_integral - middle_rectangles)
    trapezoid_discrepancy = abs(precise_integral - trapezoid)
    simpson_discrepancy = abs(precise_integral - simpson)

    first_derivative = diff(f_expr, x)
    second_derivative = diff(f_expr, x, x)
    fourth_derivative = diff(f_expr, x, x, x, x)

    l_r_theoretical = (1 / 2) * maximum(first_derivative, x, Interval(a, b)) * (b - a) * h
    middle_theoretical = (1 / 24) * maximum(second_derivative, x, Interval(a, b)) * (b - a) * (h ** 2)
    trapezoid_theoretical = (1 / 12) * maximum(second_derivative, x, Interval(a, b)) * (b - a) * (h ** 2)
    simpson_theoretical = (1 / 2880) * maximum(fourth_derivative, x, Interval(a, b)) * (b - a) * (h ** 4)

    print_result("Left rectangles", left_rectangles, left_discrepancy, l_r_theoretical, precise_integral)
    print_result("Right rectangles", right_rectangles, right_discrepancy, l_r_theoretical, precise_integral)
    print_result("Middle rectangles", middle_rectangles, middle_discrepancy, middle_theoretical, precise_integral)
    print_result("Trapezoid rectangles", trapezoid, trapezoid_discrepancy, trapezoid_theoretical, precise_integral)
    print_result("Simpson's method", simpson, simpson_discrepancy, simpson_theoretical, precise_integral)

    values = [left_rectangles, right_rectangles, middle_rectangles, trapezoid, simpson]
    theoretical = [l_r_theoretical, l_r_theoretical, middle_theoretical, trapezoid_theoretical, simpson_theoretical]

    return values, theoretical, precise_integral


def test_with_all_methods(a, b, m):
    accuracy = 10**-10
    ##0 degree
    f = parse_expr("1")
    precise_integral = integrate(f, (x, a, b))
    f = lambdify(x, f, "numpy")
    h = (b - a) / m

    w = 0
    for j in range(1, m):
        w += f(a + j * h)

    left_rectangles = h * (f(a) + w)
    right_rectangles = h * (f(b) + w)

    q = 0
    for j in range(m):
        q += f(a + j * h + (h / 2))

    middle_rectangles = h * q

    z = f(a) + f(b)

    trapezoid = (h / 2) * (z + 2 * w)
    simpson = (h / 6) * (z + 2 * w + 4 * q)

    left_discrepancy = abs(precise_integral - left_rectangles)
    right_discrepancy = abs(precise_integral - right_rectangles)
    middle_discrepancy = abs(precise_integral - middle_rectangles)
    trapezoid_discrepancy = abs(precise_integral - trapezoid)
    simpson_discrepancy = abs(precise_integral - simpson)

    if left_discrepancy > accuracy: print("Test failed on left rectangle")
    if right_discrepancy > accuracy: print("Test failed on right rectangle")
    if middle_discrepancy > accuracy: print("Test failed on middle rectangle")
    if trapezoid_discrepancy > accuracy: print("Test failed on trapezoid")
    if simpson_discrepancy > accuracy: print("Test failed on Simpson")


    ##1 degree
    f = parse_expr("x")
    precise_integral = integrate(f, (x, a, b))
    f = lambdify(x, f, "numpy")

    w = 0
    for j in range(1, m):
        w += f(a + j * h)

    q = 0
    for j in range(m):
        q += f(a + j * h + (h / 2))

    middle_rectangles = h * q

    z = f(a) + f(b)

    trapezoid = (h / 2) * (z + 2 * w)
    simpson = (h / 6) * (z + 2 * w + 4 * q)

    middle_discrepancy = abs(precise_integral - middle_rectangles)
    trapezoid_discrepancy = abs(precise_integral - trapezoid)
    simpson_discrepancy = abs(precise_integral - simpson)

    if middle_discrepancy > accuracy: print("Test failed on middle rectangle")
    if trapezoid_discrepancy > accuracy: print("Test failed on trapezoid")
    if simpson_discrepancy > accuracy: print("Test failed on Simpson")


    ##3 degree
    f = parse_expr("1 + x + x**3")
    precise_integral = integrate(f, (x, a, b))
    f = lambdify(x, f, "numpy")

    w = 0
    for j in range(1, m):
        w += f(a + j * h)

    q = 0
    for j in range(m):
        q += f(a + j * h + (h / 2))

    middle_rectangles = h * q

    z = f(a) + f(b)

    simpson = (h / 6) * (z + 2 * w + 4 * q)

    simpson_discrepancy = abs(precise_integral - simpson)

    if simpson_discrepancy > accuracy: print("Test failed on Simpson")

    return left_rectangles, right_rectangles, middle_rectangles, trapezoid, simpson