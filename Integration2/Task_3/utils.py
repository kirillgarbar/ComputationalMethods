from sympy import parse_expr, simplify
from sympy.abc import x

function_string = "sin(x)*abs(x - 0.5)"


def legendre(n: int):
    if n == 0:
        return parse_expr("1")
    elif n == 1:
        return x
    else:
        return simplify(((2 * n - 1) / n) * legendre(n - 1) * x - ((n - 1) / n) * legendre(n - 2))