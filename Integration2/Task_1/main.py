from utils import sym_weight, f, r, print_title, a, b, poly, poly_x
from sympy.abc import x
from sympy import integrate
import scipy.integrate as integrate_precise
import numpy as np
from math import sqrt

if __name__ == "__main__":
    print_title()

    precise_integral, _ = integrate_precise.quad(f, a, b)

    # Computing moments
    moments = []
    multiplier = 1
    for _ in range(4):
        moments.append(float(integrate(sym_weight(x) * multiplier, (x, a, b))))
        multiplier *= x

    print(f"Moments: {moments}")

    # Searching for orthogonal polynom
    a1 = (moments[0]*moments[3] - moments[2]*moments[1]) / (moments[1] ** 2 - moments[2]*moments[0])
    a2 = (moments[2] ** 2 - moments[3]*moments[1]) / (moments[1] ** 2 - moments[2]*moments[0])

    print(f"Polynom: x^2 + {a1}x + {a2}")

    # Computing roots
    d = a1 ** 2 - 4 * a2

    x1 = (-1 * a1 + sqrt(d)) / 2
    x2 = (-1 * a1 - sqrt(d)) / 2

    nodes = [x2, x1]

    print(f"Nodes: {nodes}")

    # Computing formula

    x_array = []

    for row in range(len(nodes)):
        x_array.append([x ** row for x in nodes])

    A = np.linalg.solve(x_array, moments[:2])

    print(f"Coefficients: {A}")
    integral = 0
    for i, a_k in enumerate(A):
        integral += a_k * r(nodes[i])

    print(f'Integral: {integral}')
    print(f'Precise integral: {precise_integral}')
    print(f'Absolute error: {abs(precise_integral - integral)}')
    print(f'Relative error in percents: {abs((precise_integral - integral)/precise_integral)*100}')





    # Testing for x^3

    accuracy = 10 ** -12
    integral = 0
    for i, a_k in enumerate(A):
        integral += a_k * poly(nodes[i])

    precise_integral, _ = integrate_precise.quad(poly_x, a, b)

    print(f'Integral: {integral}')
    print(f'Precise integral: {precise_integral}')
    print(f'Absolute error: {abs(precise_integral - integral)}')
    print(f'Relative error in percents: {abs((precise_integral - integral)/precise_integral)*100}')

    if abs(precise_integral - integral) > accuracy:
        print("Test not passed")
    else:
        print("Test passed")
