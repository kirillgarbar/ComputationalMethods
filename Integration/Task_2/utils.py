from math import exp

task_title = "Integration task 2"
task_number = 7
function_string = "f(x) = e^x"


def f(x): return exp(x)


def zero_degree(x): return 1


def first_degree(x): return x


def second_degree(x): return 1 + x ** 2


def third_degree(x): return 1 + x + x ** 3


def print_title():
    print(task_title)
    print(f"Task number = {task_number}")
    print(f"{function_string}")
    print("\n")

