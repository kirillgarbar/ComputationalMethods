def find_first_derivatives(given_x, given_y, h):
    first_derivatives = []
    n = len(given_x) - 1
    first_derivatives.append((-3 * given_y[0] + 4 * given_y[0 + 1] - given_y[0 + 2]) / (2 * h))
    for i in range(1, n):
        first_derivatives.append((given_y[i + 1] - given_y[i - 1]) / (2 * h))
    first_derivatives.append((3 * given_y[n] - 4 * given_y[n - 1] + given_y[n - 2]) / (2 * h))

    return first_derivatives


def find_second_derivatives(given_x, given_y, h):
    second_derivatives = ["-"]
    for i in range(1, len(given_x) - 1):
        second_derivatives.append((given_y[i + 1] - 2 * given_y[i] + given_y[i - 1]) / (h ** 2))
    second_derivatives.append("-")

    return second_derivatives