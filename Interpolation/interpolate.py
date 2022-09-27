def lagrange_interpolated_value(points, table, x):
    res = 0

    for i, point in enumerate(points):
        polynom = 1
        for j, point2 in enumerate(points):
            if j != i:
                polynom *= (x - point2) / (point - point2)

        res += table[point] * polynom

    return res


def find_divided_diffs(points, table):
    table_side = len(points)
    diffs = [[0 for _ in range(table_side)] for _ in range(table_side)]

    for i, point in enumerate(points):
        diffs[i][0] = table[point]

    for j in range(1, table_side):
        for i in range(table_side - j):
            diffs[i][j] = \
                (diffs[i + 1][j - 1] - diffs[i][j - 1]) / (points[i + j] - points[i])

    return diffs


def newton_interpolated_value(points, table, x):
    diffs = find_divided_diffs(points, table)[0]
    q = 1
    polynom = 0

    for i, diff in enumerate(diffs):
        polynom += diff * q
        q *= x - points[i]

    return polynom


def interpolate_with_derivation(interpolate, points, table, f, x):
    actual_value = interpolate(points, table, x)
    expected_value = f(x)

    return actual_value, abs(expected_value - actual_value)
