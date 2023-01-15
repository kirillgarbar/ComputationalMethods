import scipy.integrate as integrate_sc
from sympy import parse_expr, simplify, lambdify
from sympy.abc import x
from Integration2.Task_2.get_roots import get_roots
from utils import function_string, legendre

start = float(input("Enter left border of the interval(A): "))
end = float(input("Enter right border of the interval(B): "))
N = int(input("Enter the number of nodes(N): "))
M = int(input("Enter the number of intervals(M): "))
h = (end - start) / M
z = [start + j * h for j in range(M + 1)]
f = lambdify(x, parse_expr(function_string))


res_legendre = lambdify(x, legendre(N), 'numpy')
legendre_roots_raw = get_roots(-1, 1, res_legendre)
print(f'Number of nodes: {N}, Number of intervals: {M}')
print(f'Nodes: {legendre_roots_raw}')
a = []
prev_legendre = lambdify(x, legendre(N - 1), 'numpy')
for root in legendre_roots_raw:
    a_k = (2 * (1 - root ** 2)) / (N ** 2 * (prev_legendre(root)) ** 2)
    a.append(a_k)
print(f'Coefficients: {a}')
print()
legendre_roots = []
for i in range(len(z) - 1):
    legendre_roots_i = []
    for raw_root in legendre_roots_raw:
        legendre_roots_i.append(((h / 2) * raw_root) + ((z[i] + z[i+1]) / 2))
    legendre_roots.append(legendre_roots_i)

res = 0
for j in range(M):
    for k in range(N):
        res += a[k] * f(legendre_roots[j][k])
res *= (h / 2)

precise_value, _ = integrate_sc.quad(f, start, end)
print(f'Integral value: {res}')
print(f'Precise integral value: {precise_value}')
print(f'Absolute error: {abs(precise_value - res)}')
print(f'Relative error in percents: {abs(precise_value - res) / abs(precise_value) * 100}')