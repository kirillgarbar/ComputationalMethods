def print_table(table_size, f, x):
    table = {}
    points = []
    for j in range(table_size):
        point = x(j)
        value = f(point)
        points.append(point)
        table[point] = value

        print(f"Point: {point}; Value: {value}")
    print("\n")
    return points, table
