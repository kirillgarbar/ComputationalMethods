def find_divided_diffs(points, table):
    table_side = len(points)
    diffs = [[0 for _ in range(table_side)] for _ in range(table_side)]

    for i, point in enumerate(points):
        diffs[i][0] = table[point]

    for j in range(1, table_side):
        for i in range(table_side - j):
            diffs[i][j] = \
                (diffs[i + 1][j - 1] - diffs[i][j - 1]) / (points[i + j] - points[i])

    return diffs[0]


def polynomial_value_at_point(points, table, point):
    diffs = find_divided_diffs(points, table)

    polynomial_value_at_point = diffs[-1]
    for k in range(1, len(diffs)):
        polynomial_value_at_point = diffs[len(diffs) - 1 - k] + (
                point - points[len(points) - 1 - k]) * polynomial_value_at_point

    return polynomial_value_at_point
