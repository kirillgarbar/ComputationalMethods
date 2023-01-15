def print_result(name, value, error, precise):
    print(f"\n{name}\n"
          f"Value: {value}; "
          f"Error: {error}; "
          f"Relative error: {error / abs(precise) * 100}; ")


def runge(value1, value2, l, r):
    return (l ** r * value2 - value1) / (l ** r - 1)


def do_runge(true_value, values1, values2, l, precisions, names):
    for i, name in enumerate(names):
        value = runge(values1[i], values2[i], l, precisions[i] + 1)
        discrepancy = abs(true_value - value)

        print_result(name, value, discrepancy, true_value)