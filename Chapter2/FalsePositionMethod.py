import numpy as np


def falsePosition(func, maxIteration, TOL, p0, p1):
    q0 = func(p0)
    q1 = func(p1)

    for i in range(2, maxIteration+1):
        p = p1 - q1*(p1 - p0)/(q1 - q0)
        print('#iteration: %d \t #startPoint: %.9f \t #endPoint: %.9f' % (i, p0, p))
        if abs(p - p1) < TOL:
            print('\n#number of iterations -->', i)
            return p
        # update
        q = func(p)
        if q*q1 < 0:
            p0 = p1
            q0 = q1
        else:
            p1 = p
            q1 = q


def function(x):
    return np.cos(x) - x


if __name__ == "__main__":
    print('#Result --> %.9f' % falsePosition(function, 100, 10**(-10), np.pi/4, 0.5))
