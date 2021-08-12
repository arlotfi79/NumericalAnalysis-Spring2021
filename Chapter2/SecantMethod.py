import numpy as np


def Newton(func, maxIteration, TOL, p0, p1):
    q0 = func(p0)
    q1 = func(p1)

    for i in range(2, maxIteration+1):
        p = p1 - q1*(p1 - p0)/(q1 - q0)
        print('#startPoint: %.9f \t #endPoint: %.9f' % (p0, p))
        if abs(p - p1) < TOL:
            print('\n#number of iterations -->', i)
            return p
        # update
        p0 = p1
        q0 = q1
        p1 = p
        q1 = func(p)


def function(x):
    return (np.log10(x))**(1/2) - x + 2


if __name__ == "__main__":
    print('#Result --> %.9f' % Newton(function, 100, 10 ** (-5), 1, 2))