from math import cos, sin, exp

task_title = "Algebraic interpolation"
task_number = 7
function_string = "f(x) = exp(-x) – x^2 / 2"
a = 0
b = 1
x = 0.65
n = 7
m = 15


def f(x): return exp(-x) - x ** 2 / 2


def x(j, m, a, b): return a + j * (b - a) / m


def print_title():
    print(task_title)
    print(f"Task number = {task_number}")
    print(f"{function_string}")
    print("\n")
