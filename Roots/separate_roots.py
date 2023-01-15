def separate_roots(f, a, b, n):
    #print("Root separations is started...")
    segments = []

    while True:
        step = (b - a) / n
        y_1 = f(a)
        x_1 = a

        while x_1 <= b - step:
            x_2 = x_1 + step
            y_2 = f(x_2)

            if y_1 * y_2 <= 0:
                segment = [x_1, x_2]
                segments.append(segment)
                #print(segment)

            y_1 = y_2
            x_1 = x_2

        #print(f"Number of segments with at least one odd root: {len(segments)}")
        if True: #input("Do you want to increase number of steps by 2 and compute the segments again? (Y/N): ") != "Y":
            break
        else:
            n *= 2
            segments.clear()
            print("Root separation is finished")
            print("\n")

    return segments