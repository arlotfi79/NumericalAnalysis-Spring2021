import numpy as np
from numpy import linalg as LA


def jacobi(a, b, maxIter, TOL):
    n = len(b)
    x = np.zeros(n)
    xo = np.zeros(n)

    k = 1
    while k <= maxIter:

        for i in range(n):
            summation = 0.0
            for j in range(n):
                if i != j:
                    summation += a[i][j] * xo[j]

            x[i] = (b[i] - summation) / a[i][i]

        if LA.norm(x - xo)/LA.norm(x) < TOL:
            return x, k

        print('Iteration No.', k, ': ', x)

        k += 1
        xo = x.copy()

        if k == maxIter + 1:
            raise ValueError('Maximum t number of iterations exceeded')


if __name__ == "__main__":
    A = np.array([
        [1, 2, 6],
        [10, 1, 3],
        [2, 8, 1],
    ])

    B = np.array([
        [11],
        [15],
        [19]
    ])

    jacobi(A, B, 100, 10e-10)

