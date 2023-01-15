import numpy as np
from sympy import parse_expr, simplify
from sympy.abc import x


def legendre(n: int):
    if n == 0:
        return parse_expr("1")
    elif n == 1:
        return x
    else:
        return simplify(((2 * n - 1) / n) * legendre(n - 1) * x - ((n - 1) / n) * legendre(n - 2))


def meler(n: int, f):
    res = 0
    nodes = []
    for j in range(1, n + 1):
        nodes.append((np.cos(((2 * j - 1) * np.pi) / (2 * n))))
    print(f'Nodes: {nodes}')
    for node in nodes:
        res += f(node)
    print(f'Coefficient: {np.pi / n}')
    return res * (np.pi / n)