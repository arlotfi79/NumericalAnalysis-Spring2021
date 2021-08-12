import numpy as np


def partialPivot(A, b):
    n = len(A)
    if b.size != n:
        raise ValueError("Incompatible sizes between Matrix A & b")

    for i in range(n - 1):
        maxIndex = abs(A[i:, i]).argmax() + i

        if A[maxIndex, i] == 0:
            raise ValueError("Matrix is singular.")

        if maxIndex != i:
            A[[i, maxIndex]] = A[[maxIndex, i]]
            b[[i, maxIndex]] = b[[maxIndex, i]]
        for row in range(i + 1, n):
            multiplier = A[row][i] / A[i][i]
            A[row][i] = multiplier
            for col in range(i + 1, n):
                A[row][col] = A[row][col] - multiplier * A[i][col]

            b[row] = b[row] - multiplier * b[i]

    x = np.zeros(n)
    i = n - 1
    x[i] = b[i] / A[i, i]

    for i in range(n-1, -1, -1):
        x[i] = (b[i] - np.dot(A[i, i + 1:], x[i + 1:])) / A[i, i]

    return x


if __name__ == "__main__":
    AMat = np.array([
        [2.11, -4.21, 0.921],
        [4.01, 10.2, -1.12],
        [1.09, 0.987, 0.832]
    ])

    bMat = np.array([
        [2.01],
        [-3.09],
        [4.21]
    ])

    Xs = partialPivot(AMat, bMat)
    print('x1 = %f \nx2 = %f \nx3 = %f' % (Xs[0], Xs[1], Xs[2]))
