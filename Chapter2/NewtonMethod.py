import numpy as np


def newton(func, funcPrime, maxIteration, TOL, p0):
    for i in range(maxIteration):
        p = p0 - func(p0)/funcPrime(p0)
        print('#startPoint: %.9f \t #endPoint: %.9f' % (p0, p))
        if abs(p - p0) < TOL:
            print('\n#number of iterations -->', i)
            return p
        p0 = p


def function(x):
    return (np.log10(x))**(1/2) + 2


def functionPrime(x):
    return (1/x)*(1/2)*(np.log10(x))**(-1/2)


if __name__ == "__main__":
    print('#Result --> %.5f' % newton(function, functionPrime, 100, 10**(-5), np.pi/4))
