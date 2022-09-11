def bisection_method(f, segments, accuracy):
    roots = []

    for segment in segments:
        a = segment[0]
        b = segment[1]
        steps = 0

        while b - a > 2 * accuracy:
            c = (a + b) / 2
            if f(a) * f(c) <= 0:
                b = c
            else:
                a = c
            steps += 1

        x = (a + b) / 2
        delta = abs(b - a)
        roots.append([x, delta, steps])

    return roots


def newtons_method(f, derivative_of_f, segments, accuracy):
    roots = []

    for segment in segments:
        steps = 0
        current_point = segment[0]
        previous_point = None

        while previous_point is None or abs(current_point - previous_point) >= accuracy:
            previous_point = current_point
            current_point = previous_point - f(previous_point) / derivative_of_f(previous_point)
            steps += 1

        delta = abs(current_point - previous_point)
        roots.append([current_point, delta, steps])

    return roots


def modified_newtons_method(f, derivative_of_f, segments, accuracy):
    roots = []

    for segment in segments:
        steps = 0
        current_point = segment[0]
        previous_point = None
        starting_point_derivative = derivative_of_f(current_point)

        while previous_point is None or abs(current_point - previous_point) >= accuracy:
            previous_point = current_point
            current_point = previous_point - f(previous_point) / starting_point_derivative
            steps += 1

        delta = abs(current_point - previous_point)
        roots.append([current_point, delta, steps])

    return roots


def secant_method(f, segments, accuracy):
    roots = []

    for segment in segments:
        steps = 0
        current_point = segment[0]
        previous_point = None

        while previous_point is None or abs(current_point - previous_point) > accuracy:
            if previous_point is None:
                previous_previous_point = segment[1]
            else:
                previous_previous_point = previous_point
            previous_previous_function_value = f(previous_previous_point)

            previous_point = current_point
            previous_function_value = f(previous_point)

            current_point = previous_point - previous_function_value * (previous_point - previous_previous_point) / (
                    previous_function_value - previous_previous_function_value
            )

            steps += 1

        delta = abs(current_point - previous_point)
        roots.append([current_point, delta, steps])

    return roots


def reduce_roots(f, derivative_of_f, segments, accuracy):
    print("""
There are 4 different methods to reduce roots
1. Bisection method
2. Newton's method
3. Modified Newton's method
4. Secant method
        """)
    method = int(input("Enter the number of the method (1, 2, 3, 4): "))
    roots = []
    method_name = ""
    if method == 1:
        roots = bisection_method(f, segments, accuracy)
        method_name = "Bisection Method\n"
    elif method == 2:
        roots = newtons_method(f, derivative_of_f, segments, accuracy)
        method_name = "Newton's Method\n"
    elif method == 3:
        roots = modified_newtons_method(f, derivative_of_f, segments, accuracy)
        method_name = "Modified Newton's Method\n"
    elif method == 4:
        roots = secant_method(f, segments, accuracy)
        method_name = "Secant Method\n"
    else: print("No such method")

    #Printing the results
    print(method_name)
    for i in range(len(roots)):
        root = roots[i]
        print(f"Root number: {i + 1}")
        print(f"Starting approximation: {segments[i]}")
        print(f"Number of steps: {root[2]}")
        print(f"Root: {root[0]}")
        print(f"Accuracy: {root[1]}")
        print(f"Absolute derivation from 0: {abs(f(root[0]))}\n")
