def midPoint(a, b, alphaCond, n, func):
    # Step 1
    h = (b - a) / n
    t = a
    w = alphaCond
    print('\tti \t\t\t\t wi \n--------------------------------\n%.10f \t %.10f ' % (t, w))

    # Step 2
    for i in range(1, n + 1):
        # Step 3
        w += h * func(t + h/2, w + h/2 * func(t, w))
        t = a + i * h

        # Step 4
        print('%.10f \t %.10f ' % (t, w))


def function(t, y):
    return y - t ** 2 + 1


if __name__ == "__main__":
    # Interval
    A = 0
    B = 2
    # Condition
    Alpha = 0.5  # y(0) = 0.5
    # Step Segments
    N = 10

    midPoint(A, B, Alpha, N, function)
