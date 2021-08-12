def simpson(a, b, n, func):
    h = (b - a)/n

    XI0 = func(a) + func(b)
    XI1 = 0
    XI2 = 0

    for i in range(1, n):
        X = a + i*h

        if i % 2 == 0:
            XI2 += func(X)
        else:
            XI1 += func(X)

    XI = h * (XI0 + 2*XI2 + 4*XI1)/3
    return XI


def function(x):
    return x**2


if __name__ == "__main__":
    print('Approximation Result: %.10f' % simpson(0, 3.5, 6, function))
