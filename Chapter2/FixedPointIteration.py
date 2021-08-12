def fixedPointIteration(func, maxIteration, TOL, p0):
    for i in range(maxIteration):
        p = func(p0)
        print('#startPoint: %f \t #endPoint: %f' % (p0, p))

        if abs(p - p0) < TOL:
            print('\n#number of iterations -->', i)
            return p
        p0 = p


def functionQ7(x):
    return (3 * x ** 2 + 3) ** (1 / 4)


def functionQ11(y):
    return (1 / 2) * (y + 3 / y)


if __name__ == "__main__":
    print('Question 7')
    print('#Result --> %.10f' % fixedPointIteration(functionQ7, 100, 10 ** (-2), 1))

    print('\nQuestion 11')
    print('#Result --> %.10f' % fixedPointIteration(functionQ11, 100, 10 ** (-4), 1))
