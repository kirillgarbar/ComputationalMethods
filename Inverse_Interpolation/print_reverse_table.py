def print_reverse_table(points, table):
    new_table = {}
    new_points = []
    for i, point in enumerate(points):
        value = table[point]
        new_points.append(value)
        new_table[value] = point

        print(f"Point: {value}; Value: {point}")
    print("\n")
    return new_points, new_table
