from utils import a, b, print_title, f, nodes, r, weight, sym_weight
from sympy.abc import x
from sympy import integrate
import numpy as np
import scipy.integrate as integrate_precise


if __name__ == '__main__':
    print_title()

    precise_integral, _ = integrate_precise.quad(f, a, b)

    weights = []
    multiplier = 1
    for node in nodes:
        weights.append(float(integrate(sym_weight(x) * multiplier, (x, a, b))))
        multiplier *= x

    x_array = []

    for row in range(len(nodes)):
        x_array.append([x ** row for x in nodes])

    A = np.linalg.solve(x_array, weights)

    print(f"Coefficients: {A}")
    integral = 0
    for i, a_k in enumerate(A):
        integral += a_k * r(nodes[i])

    print(f'Integral: {integral}')
    print(f'Precise integral: {precise_integral}')
    print(f'Absolute error: {abs(precise_integral - integral)}')
    print(f'Relative error in percents: {abs((precise_integral - integral)/precise_integral)*100}')