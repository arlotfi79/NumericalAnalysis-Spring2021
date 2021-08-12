import numpy as np


def luDecomposition(mat, n):
    lower = np.zeros((n, n))
    upper = np.zeros((n, n))

    for i in range(n):
        # Upper
        for k in range(i, n):
            summation = 0
            for j in range(i):
                summation += (lower[i][j] * upper[j][k])

            upper[i][k] = mat[i][k] - summation

        # Lower
        for k in range(i, n):
            if i == k:
                lower[i][i] = 1
            else:
                summation = 0
                for j in range(i):
                    summation += (lower[k][j] * upper[j][i])

                lower[k][i] = int((mat[k][i] - summation) / upper[i][i])

    return lower, upper


def printResult(mat, n):
    for i in range(n):
        print(mat[i][:])


if __name__ == "__main__":

    # Augmented Matrix A | B
    A = np.array([
        [1, 1, 0, 3, 4],
        [2, 1, -1, 1, 1],
        [3, -1, -1, 2, -3],
        [-1, 2, 3, -1, 4]
    ])

    # b = np.array([
    #     [4],
    #     [1],
    #     [-3],
    #     [4]
    # ])

    N = len(A)

    Lower, Upper = luDecomposition(A, N)
    print('Lower Matrix')
    printResult(Lower, N)
    print('--------------------------------')
    print('Upper matrix')
    printResult(Upper, N)
