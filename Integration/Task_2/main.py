from utils import *
from scipy import integrate
from integration_methods import *

if __name__ == '__main__':
    print_title()

    a = float(input("Enter left border of the interval: "))
    b = float(input("Enter right border of the interval: "))

    while b <= a:
        b = float(input("Right border must be greater than left. Try again: "))

    print("\n")
    precise_integral, _ = integrate.quad(f, a, b)
    print(f"Precise integral value: {precise_integral}")
    print("\n")

    print("Left rectangle method")
    integrate_with_method(left_rectangle_method, f, a, b, precise_integral)
    print("\n")

    print("Right rectangle method")
    integrate_with_method(right_rectangle_method, f, a, b, precise_integral)
    print("\n")

    print("Middle rectangle method")
    integrate_with_method(middle_rectangle_method, f, a, b, precise_integral)
    print("\n")

    print("Trapezoid method")
    integrate_with_method(trapezoid_method, f, a, b, precise_integral)
    print("\n")

    print("Simpson's method")
    integrate_with_method(simpsons_method, f, a, b, precise_integral)
    print("\n")

    print("3/8 method")
    integrate_with_method(three_eights_method, f, a, b, precise_integral)
    print("\n")


    print("Testing degrees of accuracy\n")
    a = 0
    b = 10
    accuracy = pow(10, -20)
    print("Zero degree")
    f = zero_degree
    expected = b - a

    if discrepancy(left_rectangle_method(f, a, b), expected) > accuracy: print("Test failed on left rectangular method")

    if discrepancy(right_rectangle_method(f, a, b), expected) > accuracy: print("Test failed on right rectangular method")

    if discrepancy(middle_rectangle_method(f, a, b), expected) > accuracy: print("Test failed on middle rectangular method")

    if discrepancy(trapezoid_method(f, a, b), expected) > accuracy: print("Test failed on trapezoid method")

    if discrepancy(simpsons_method(f, a, b), expected) > accuracy: print("Test failed on Simpson's method")

    if discrepancy(three_eights_method(f, a, b), expected) > accuracy: print("Test failed on 3/8 method")
    print("\n")

    print("First degree")
    f = first_degree
    expected, _ = integrate.quad(f, a, b)

    if discrepancy(middle_rectangle_method(f, a, b), expected) > accuracy: print(
        "Test failed on middle rectangular method")

    if discrepancy(trapezoid_method(f, a, b), expected) > accuracy: print("Test failed on trapezoid method")

    if discrepancy(simpsons_method(f, a, b), expected) > accuracy: print("Test failed on Simpson's method")

    if discrepancy(three_eights_method(f, a, b), expected) > accuracy: print("Test failed on 3/8 method")
    print("\n")

    print("Second degree")
    f = second_degree
    expected, _ = integrate.quad(f, a, b)

    if discrepancy(simpsons_method(f, a, b), expected) > accuracy: print("Test failed on Simpson's method")

    if discrepancy(three_eights_method(f, a, b), expected) > accuracy: print("Test failed on 3/8 method")
    print("\n")

    print("Third degree")
    f = third_degree
    expected, _ = integrate.quad(f, a, b)

    if discrepancy(simpsons_method(f, a, b), expected) > accuracy: print("Test failed on Simpson's method")

    if discrepancy(three_eights_method(f, a, b), expected) > accuracy: print("Test failed on 3/8 method")
    print("\n")