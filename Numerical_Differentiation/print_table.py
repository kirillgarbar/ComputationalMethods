from tabulate import tabulate
from find_derivative import *
from utils import *


def print_table(table):
    table_rows = []
    header_row = ["x", "f(x)"]
    table_rows.append(header_row)
    for pair in table:
        table_rows.append([pair[0], pair[1]])

    print(tabulate(table_rows))


def print_results_table(table_of_values, h):
    given_x = [pair[0] for pair in table_of_values]
    given_y = [pair[1] for pair in table_of_values]
    first_derivatives = find_first_derivatives(given_x, given_y, h)
    second_derivatives = find_second_derivatives(given_x, given_y, h)
    table = []
    first_row = ["x_i", "f(x_i)", "f'(x_i)_чд", "|f'(x_i)_т - f'(x_i)_чд|", "процент ошибки f'", "f''(x_i)_чд" , "|f''(x_i)_т - f''(x_i)_чд|", "процент ошибки f\""]
    table.append(first_row)

    for i in range(len(table_of_values)):
        x_i = given_x[i]
        y_i = given_y[i]
        first_derivative = first_derivatives[i]
        second_derivative = second_derivatives[i]
        given_first_derivative = first_der_f(x_i)
        given_second_derivative = second_der_f(x_i)
        first_diff = abs(given_first_derivative - first_derivative)
        first_rel_diff = first_diff / given_first_derivative * 100
        if second_derivative != "-":
            second_diff = abs(given_second_derivative - second_derivative)
            second_rel_diff = second_diff / given_second_derivative * 100
        else:
            second_diff = "-"
            second_rel_diff = "-"
        current_row = [x_i, y_i, first_derivative, first_diff, first_rel_diff, second_derivative, second_diff, second_rel_diff]
        table.append(current_row)

    print(tabulate(table))