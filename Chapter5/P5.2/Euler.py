import numpy as np


def euler(a, b, n, alphaCond, func):
    # Step 1
    h = (b - a) / n
    t = a
    w = alphaCond
    print('\tti \t\t\t\t wi \n--------------------------------\n%.10f \t %.10f ' % (t, w))

    # Step 2
    for i in range(1, n + 1):
        # Step 3
        w = w + h * func(t, w)
        t = a + i * h

        # Step 4
        print('%.10f \t %.10f ' % (t, w))


def function(t, y):
    return (1/2)*np.exp(y) + (1/2)*np.exp(-y)


if __name__ == "__main__":
    # Interval
    A = 0
    B = 1
    # Condition
    Alpha = 0  # y(0) = 0.5
    # Step Segments
    N = 2

    euler(A, B, N, Alpha, function)
    print(function(0, 1))




