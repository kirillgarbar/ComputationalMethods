def print_table(f, table_size, a, b):
    table = {}
    points = []
    h = (b - a) / (table_size - 1)
    for j in range(table_size):
        point = a + j * h
        value = f(point)
        points.append(point)
        table[point] = value

        print(f"Point: {point}; Value: {value}")
    print("\n")
    return points, table
