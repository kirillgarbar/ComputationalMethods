from math import cos, sin, exp

task_title = "Inverse algebraic interpolation"
task_number = 7
function_string = "f(x) = exp(-x) – x^2 / 2"
a = 0
b = 1
x = 0.65
n = 7
m = 15


def f(x): return exp(-x) - x ** 2 / 2


def p(diffs, points, x):
    polynom = 0
    q = 1

    for i, diff in enumerate(diffs):
        polynom += diff * q
        q *= x - points[i]


def print_title():
    print(task_title)
    print(f"Task number = {task_number}")
    print(f"{function_string}")
    print("\n")
