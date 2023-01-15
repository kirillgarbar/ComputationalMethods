from integrate import integrate_with_all_methods, test_with_all_methods
from sympy import parse_expr

if __name__ == "__main__":

    f = parse_expr(input("Enter the function: "))

    a = float(input("Enter left border of the interval: "))
    b = float(input("Enter right border of the interval: "))

    while b <= a:
        b = float(input("Right border must be greater than left. Try again: "))

    m = int(input("Enter the number of intervals: "))

    integrate_with_all_methods(a, b, m, f)

    print("Executing tests...\n")

    test_with_all_methods(a, b, m)
