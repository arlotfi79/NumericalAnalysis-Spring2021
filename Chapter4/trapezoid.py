import numpy as np


def trapezoid(a, b, n, func):
    h = (b - a) / n

    res = func(a)
    for i in range(1, n):
        res = res + 2 * func(a + i * h)

    res = res + func(b)

    return res * h / 2


def function(x):
    return np.sin(x)


if __name__ == "__main__":
    test = trapezoid(0, 2, 50, function)
    if (6.09172981 * 10e-4 - test) <= (2 / 3) * 10e-4:
        print('true')
    else:
        print('false')
