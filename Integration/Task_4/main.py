from Integration.Task_3.integrate import integrate_with_all_methods
from sympy import parse_expr
from runge import do_runge

if __name__ == "__main__":

    f = parse_expr(input("Enter the function: "))

    a = float(input("Enter left border of the interval: "))
    b = float(input("Enter right border of the interval: "))

    while b <= a:
        b = float(input("Right border must be greater than left. Try again: "))

    m = int(input("Enter the number of intervals(m): "))
    l = int(input("Enter the multiplier of m(l):"))

    print("\n")

    print("Integrating for m partitions:")
    values1, theoretial, true_value = integrate_with_all_methods(a, b, m, f)
    print("\n")
    print("Integrating for m * l partitions:")
    values2, _, _ = integrate_with_all_methods(a, b, m * l, f)

    precision = [0, 0, 1, 1, 3]
    names = ["Left rectangle", "Right rectangle", "Middle rectangle", "Trapezoid", "Simpon's"]

    print("\n")

    print("Refining with Runge:")

    do_runge(true_value, values1, values2, l, precision, names)