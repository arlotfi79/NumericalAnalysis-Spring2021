import numpy as np


def scaledPivot(A, b, n):
    L = np.zeros(n, dtype=int)
    S = np.zeros(n, dtype=float)
    X = np.zeros(n, dtype=float)

    for i in range(n):
        L[i] = i
        sMax = 0.0
        for j in range(n):
            if abs(A[i][j]) > sMax:
                sMax = abs(A[i][j])
        S[i] = sMax

    for i in range(n - 1):
        rMax = 0.0
        for j in range(i, n):
            ratio = abs(A[L[j]][i]) / S[L[j]]
            if ratio > rMax:
                rMax = ratio
                rIndex = j

        temp = L[i]
        L[i] = L[rIndex]
        L[rIndex] = temp

        for j in range(i + 1, n):
            multiplier = A[L[j]][i] / A[L[i]][i]
            for k in range(i, n):
                A[L[j]][k] = A[L[j]][k] - multiplier * A[L[i]][k]
            b[L[j]] = b[L[j]] - multiplier * b[L[i]]

    X[n - 1] = b[L[n - 1]] / A[L[n - 1]][n - 1]
    for j in range(n - 2, -1, -1):
        summation = 0.0
        for k in range(j + 1, n):
            summation = summation + A[L[j]][k] * X[k]
        X[j] = (b[L[j]] - summation) / A[L[j]][j]

    return X


if __name__ == "__main__":
    AMat = np.array([
        [2, 1, 3],
        [4, 6, 8],
        [6, 6, 10]
    ])

    bMat = np.array([
        [1],
        [5],
        [5]
    ])

    Xs = scaledPivot(AMat, bMat, 3)
    print('x1 = %f \nx2 = %f \nx3 = %f' % (Xs[0], Xs[1], Xs[2]))
