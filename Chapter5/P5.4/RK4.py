from math import exp


def RK4(a, b, alphaCond, n, func, exFunc):
    # Step 1
    h = (b - a) / n
    t = a
    w = alphaCond
    print('\tNode \t\t Approximation y \t Exact y \t Exact y - Approximation y '
          '\n--------------------------------------------------------------------\n%.10f \t %.10f \t '
          '%.10f \t %.10f' % (t, w, exFunc(t), exFunc(t) - w))

    # Step 2
    for i in range(1, n + 1):
        # Step 3
        k1 = h * (func(t, w))
        k2 = h * (func((t + h / 2), (w + k1 / 2)))
        k3 = h * (func((t + h / 2), (w + k2 / 2)))
        k4 = h * (func((t + h), (w + k3)))

        # Step 4
        w += (k1 + 2 * k2 + 2 * k3 + k4) / 6
        t = a + i * h

        # Step 5
        print('%.10f \t %.10f \t %.10f \t %.10f' % (t, w, exFunc(t), exFunc(t) - w))


def function(t, y):
    return -(y + 1) * (y + 3)


def function2(t, y):
    return -5 * y + 5 * (t ** 2) + 2 * t


def exactFunction(t):
    return -3 + 2 * ((1 + exp(2 * t)) ** (-1))


def exactFunction2(t):
    return t ** 2 + (1 / 3) * exp(-5 * t)


if __name__ == "__main__":
    # Interval
    A = 0
    B = 2
    # Condition
    Alpha = -2  # y(0) = 0.5
    # Step Segments
    N = 10

    print('Part A')
    RK4(A, B, Alpha, N, function, exactFunction)
    # -------------------------------------------------------------
    # Interval
    A2 = 0
    B2 = 1
    # Condition
    Alpha2 = 1 / 3  # y(0) = 0.5
    # Step Segments
    N2 = 10

    print('\nPart B\n')
    RK4(A, B, Alpha, N, function, exactFunction)
