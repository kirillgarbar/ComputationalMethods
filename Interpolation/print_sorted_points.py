def print_sorted_points(points, x):
    distances = []
    for point in points:
        distances.append([abs(x - point), point])

    result = sorted(distances)
    for pair in result: print(f"Point: {pair[1]}; Distance from X: {pair[0]}")

    return [pair[1] for pair in result]
