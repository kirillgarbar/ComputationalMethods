from utils import *
from Inverse_Interpolation.print_table import print_table
from print_reverse_table import print_reverse_table
from Interpolation.print_sorted_points import print_sorted_points
from Interpolation.interpolate import interpolate_with_derivation, lagrange_interpolated_value, newton_interpolated_value
from bisection_method_inverse_interpolation import bisection_method_inverse_interpolation

if __name__ == '__main__':
    print_title()

    a = int(input("Enter the left border of interval: "))
    b = int(input("Enter the right border of interval: "))
    table_size = int(input("Enter the number of values in the table: "))
    print("\n")
    points, table = print_table(f, table_size, a, b)

    print("Reversed table(for monotonous function only)\n")
    rev_points, reversed_table = print_reverse_table(points, table)

    while True:
        X = float(input("Enter the value of f(x) to perform inverse interpolation: "))
        n = int(input(f"Enter the degree of the polynom(Lesser than {table_size}): "))
        while n >= table_size:
            n = int(input("Wrong degree. Try again: "))
            print("\n")
        sorted_points = print_sorted_points(rev_points, X)

        value, _ = interpolate_with_derivation(newton_interpolated_value, sorted_points[:n + 1], reversed_table, f, X)
        derivation = abs(f(value) - X)
        print(f"Inverse interpolation result using reversed table: {value}")
        print(f"Absolute derivation from expected value: {derivation}")
        print("\n")

        print("Now, assuming function is not monotonous\n")

        accuracy = float(input("Enter accuracy: "))

        sorted_points = print_sorted_points(points, X)
        bisection_method_inverse_interpolation(a, b, accuracy, sorted_points[:n + 1], table, X)

        if input("Do you want to enter new point of interpolation?(Y/N): ") != "Y":
            break
