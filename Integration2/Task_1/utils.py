from math import exp, sqrt

from sympy import sqrt as sym_sqrt

task_title = "Integration task 5.1"
task_number = 7
function_string = "f(x) = exp(x)"
weight_string = "weight(x) = sqrt(1 - x)"
a = 0
b = 1


def r(x): return exp(x)


def sym_weight(x): return sym_sqrt(1 - x)


def f(x): return sqrt(1 - x) * r(x)


def poly(x): return x ** 3


def poly_x(x): return x ** 3 * sqrt(1 - x)


def print_title():
    print(task_title)
    print(f"Task number = {task_number}")
    print(f"{function_string}")
    print(f"Left border = {a}")
    print(f"Right border = {b}")
    print(f"{weight_string}")
    print("\n")