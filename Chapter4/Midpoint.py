import numpy as np


def midpoint(a, b, n, func):
    h = float(b - a) / n
    result = 0
    for i in range(n):
        result += func((a + h / 2.0) + i * h)
    result *= h
    return result


def function(x):
    return np.sin(x)


if __name__ == "__main__":
    print('Approximation Result for Midpoint Method: %.10f' % midpoint(0, np.pi/4, 1, function))
