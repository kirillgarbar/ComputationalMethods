import argparse
from fractions import Fraction

import scipy.integrate as integrate_sc 
import numpy as np

from sympy import parse_expr, integrate, lambdify
from sympy.abc import x

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--F")
    parser.add_argument("--W")
    parser.add_argument("--A")
    parser.add_argument("--B")
    parser.add_argument("--nodes")
    args = parser.parse_args()
    nodes = args.nodes.split(',')
    nodes = list(map(float, map(Fraction, nodes)))

    f_expr = parse_expr(args.F)
    weight_expr = parse_expr(args.W)
    start, end = float(args.A), float(args.B)

    integral_expr = f_expr * weight_expr

    f = lambdify(x, f_expr, "numpy")
    weight_f = lambdify(x, weight_expr, "numpy")
    integral_f = lambdify(x, integral_expr, "numpy")
    ground_truth, _ = integrate_sc.quad(integral_f, start, end)

    weights = []
    multiplier = 1
    for node in nodes:
        weights.append(float(integrate(weight_expr * multiplier, (x, start, end))))
        multiplier *= x

    matrix = np.empty((len(nodes), len(nodes)))
    nodes = np.asarray(nodes)
    for i in range(len(nodes)):
        matrix[i] = nodes ** i

    A = np.linalg.solve(matrix, weights)

    result = 0
    for i, a_k in enumerate(A):
        result += a_k * f(nodes[i])

    print(f'Integration result: {result}')
    print(f'Error: {abs(ground_truth - result)}')
