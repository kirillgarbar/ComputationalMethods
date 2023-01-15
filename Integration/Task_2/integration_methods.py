def left_rectangle_method(function, a, b):
    return (b - a) * function(a)


def right_rectangle_method(function, a, b):
    return (b - a) * function(b)


def middle_rectangle_method(function, a, b):
    return (b - a) * function((a + b) / 2.0)


def trapezoid_method(function, a, b):
    return ((b - a) / 2) * (function(a) + function(b))


def simpsons_method(function, a, b):
    return ((b - a) / 6) * (function(a) + 4 * function((a + b) / 2) + function(b))


def three_eights_method(function, a, b):
    h = (b - a) / 3
    return (b - a) * (
            (1 / 8) * function(a) + (3 / 8) * function(a + h) +
            (3 / 8) * function(a + 2 * h) + (1 / 8) * function(b)
    )


def discrepancy(actual, expected): return abs(actual - expected)


def print_discrepancy(actual, expected):
    print(f"Absolute actual discrepancy: {abs(actual - expected)}")


def integrate_with_method(method, f, a, b, expected):
    integral = method(f, a, b)
    print(f"Integral value: {integral}")
    print_discrepancy(integral, expected)
