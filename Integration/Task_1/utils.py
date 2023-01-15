from math import exp, sqrt

import sympy

task_title = "Integration task 1"
task_number = 7
function_string = "f(x) = exp(x) * sqrt(1 - x)"
weight_string = "weight(x) = sqrt(1 - x)"
a = 0
b = 1
nodes = [0, 0.1, 0.2, 1]

def r(x): return exp(x)


def weight(x): return sqrt(1 - x)


def sym_weight(x): return sympy.sqrt(1 - x)


def f(x): return r(x) * weight(x)


def print_title():
    print(task_title)
    print(f"Task number = {task_number}")
    print(f"{function_string}")
    print(f"Left border = {a}")
    print(f"Right border = {b}")
    print(f"Weight = {weight_string}")
    print(f"Nodes = {nodes}")
    print("\n")