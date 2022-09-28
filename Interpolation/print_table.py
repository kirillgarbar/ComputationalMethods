def print_table(table_size, f, x, m, a, b):
    table = {}
    points = []
    for j in range(table_size):
        point = x(j, m, a, b)
        value = f(point)
        points.append(point)
        table[point] = value

        print(f"Point: {point}; Value: {value}")
    print("\n")
    return points, table
