from utils import *
from print_table import print_table
from print_sorted_points import print_sorted_points
from interpolate import *

if __name__ == '__main__':
    print_title()

    a = int(input("Enter the left border of interval: "))
    b = int(input("Enter the right border of interval: "))
    table_size = int(input("Enter the number of values in the table: "))
    print("\n")
    points, table = print_table(table_size, f, x, table_size - 1, a, b)

    while True:
        X = float(input("Enter the point of interpolation: "))
        n = int(input(f"Enter the degree of the polynom(Lesser than {table_size}): "))
        print("\n")
        while n >= table_size:
            n = int(input("Wrong degree. Try again: "))
            print("\n")
        sorted_points = print_sorted_points(points, X)
        print("\n")

        value, derivation = interpolate_with_derivation(lagrange_interpolated_value, sorted_points[:n + 1], table, f, X)
        print(f"Value of Lagrange's interpolation polynom: {value}")
        print(f"Absolute derivation from expected value: {derivation}")
        print("\n")

        value, derivation = interpolate_with_derivation(newton_interpolated_value, sorted_points[:n + 1], table, f, X)
        print(f"Value of Newton's interpolation polynom: {value}")
        print(f"Absolute derivation from expected value: {derivation}")
        print("\n")

        if input("Do you want to enter new point of interpolation?(Y/N): ") != "Y":
            break

