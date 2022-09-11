from math import cos, sin

task_title = "Numerical methods for solving nonlinear equations"
function_string = "f(x) = 10 * cos(x) - 0.1 * x^2"
start = -8
end = 2
default_steps = 10 ** 3
accuracy = 10 ** -5


def f(x): return 10 * cos(x) - 0.1 * (x ** 2)


def derivative_of_f(x): return -10 * sin(x) - 0.2 * x


def print_title():
    print(task_title)
    print(f"A = {start}")
    print(f"B = {end}")
    print(function_string)
    print(f"Epsilon = {accuracy}")
    print("\n")

