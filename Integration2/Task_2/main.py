import numpy as np
import scipy.integrate as integrate_sc
from sympy import parse_expr, simplify, lambdify
from sympy.abc import x
from utils import legendre, meler

from get_roots import get_roots

Ns = [4, 5, 7, 8]
expr = "(x + 0.8) / sqrt(x ** 2 + 1,2)"
expr = lambdify(x, parse_expr(expr), 'numpy')

start = float(input("Enter left border of the interval: "))
end = float(input("Enter right border of the interval: "))

while start > end:
    end = float(input("Right border must be greater than left. Try again: "))

print("Legendre")
for i in range(1, 9):
    res_legendre = lambdify(x, legendre(i), 'numpy')
    legendre_roots_raw = get_roots(-1, 1, res_legendre)
    a_ = []
    prev_legendre = lambdify(x, legendre(i - 1), 'numpy')
    for root in legendre_roots_raw:
        a_k = (2 * (1 - root ** 2)) / (i ** 2 * (prev_legendre(root)) ** 2)
        a_.append(a_k)
    print(f'Number of nodes = {i}')
    sum = 0
    for root, coeff in zip(legendre_roots_raw, a_):
        sum += coeff
        print(f'Root: {root}; coeff: {coeff}')
    print(f'Sum of coeffs: {sum}')
    print("\n")
print('----------------------------------------------------')

for N in Ns:
    print(f'Number of nodes = {N}')
    res_legendre = lambdify(x, legendre(N), 'numpy')
    legendre_roots_raw = get_roots(-1, 1, res_legendre)
    legendre_roots = []
    for raw_root in legendre_roots_raw:
        legendre_roots.append((((end - start) / 2) * raw_root) + ((end + start) / 2))

    print(f'Found roots: {legendre_roots}')
    a = []
    prev_legendre = lambdify(x, legendre(N - 1), 'numpy')
    for root in legendre_roots_raw:
        a_k = (2 * (1 - root ** 2)) / (N ** 2 * (prev_legendre(root)) ** 2)
        a.append(a_k)

    a = np.asarray(a) * ((end - start) / 2)
    print(f'Found coeffs: {a}')

    integral = 0
    for i, root in enumerate(legendre_roots):
        integral += a[i] * expr(root)

    precise_value, _ = integrate_sc.quad(expr, start, end)
    print(f'Integral value: {integral}')
    print(f'Precise integral value: {precise_value}')
    print(f'Absolute error: {abs(precise_value - integral)}')
    print(f'Relative error in percents: {abs(precise_value - integral) / abs(precise_value) * 100}')
    print('\n')
print('----------------------------------------------------')

print('Meler:')
meler_Ns = input("Enter the degrees(a, b, c): ").split(',')
meler_Ns = list(map(int, meler_Ns))
meler_expr = 'exp(2*x) * (x ** 2)'
meler_f = lambdify(x, parse_expr(meler_expr), 'numpy')
meler_full = lambdify(x, parse_expr('(exp(2*x) * (x ** 2)) / sqrt(1 - x ** 2)'), 'numpy')
precise_value, _ = integrate_sc.quad(meler_full, -1, 1)
for N in meler_Ns:
    meler_found = meler(N, meler_f)
    print(f'Number of nodes = {N}')
    print(f'Found Meler value: {meler_found}')
    print(f'Absolute error: {abs(precise_value - meler_found)}')
    print(f'Relative error in percents: {abs(precise_value - meler_found) / abs(precise_value) * 100}')
    print('\n')
