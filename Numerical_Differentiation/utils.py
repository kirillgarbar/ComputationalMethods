from math import cos, sin, exp

task_title = "Numerical differentiation"
task_number = 7
function_string = "f(x) = exp(4.5 * x)"


def f(x): return exp(1.5 * x * 3)

def first_der_f(x): return 4.5 * f(x)

def second_der_f(x): return 4.5 * 4.5 * f(x)


def print_title():
    print(task_title)
    print(f"Task number = {task_number}")
    print(f"{function_string}")
    print("\n")
