import numpy as np
from print_table import *

from utils import *


if __name__ == "__main__":
    print_title()

    while True:
        a = float(input("Enter the start point: "))
        h = float(input("Enter the step: "))
        number_of_values = int(input("Enter the number of values: "))
        m = number_of_values - 1

        formula_for_x_i = lambda i: a + i * h

        b = formula_for_x_i(m)
        given_x_range = np.arange(a, b + h, h)

        print(f"Number of values: {number_of_values}")
        print()
        table_of_values = [(x, f(x)) for x in [formula_for_x_i(i) for i in range(0, number_of_values)]]
        print("Table of values:")
        print_table(table_of_values)
        print("Results table:")
        print_results_table(table_of_values, h)

        if input("Do you want to run the program again?(Y/N): ") != "Y":
            break