# using zeros() to create empty array and fabs() to get absolute value
from numpy import array, zeros, fabs


def GaussianPivot(a, b, x, n):
    # Elimination
    for k in range(n - 1):
        if fabs(a[k, k] < 1.0e-12):
            for i in range(k + 1, n):
                if fabs(a[i, k] > fabs(a[k, k])):
                    a[[k, i]] = a[[i, k]]
                    b[[k, i]] = b[[i, k]]
                    break

        for i in range(k + 1, n):
            if a[i, k] == 0:
                continue

            factor = a[k, k] / a[i, k]
            for j in range(k, n):
                a[i, j] = a[k, j] - a[i, j] * factor
            b[i] = b[k] - b[i] * factor

    print('a:\n', a)
    print('b:\n', b)

    # BackSubstitution
    x[n - 1] = b[n - 1] / a[n - 1, n - 1]
    for i in range(n - 2, -1, -1):
        sumAX = 0
        for j in range(i + 1, n):
            sumAX += a[i, j] * x[j]
        x[i] = (b[i] - sumAX) / a[i, i]


if __name__ == "__main__":
    a = array([[13, 17, 1],
               [0, 1, 19],
               [0, 12, -1]], float)

    b = array([5, 1, 0])

    n = len(b)
    x = zeros(n, float)

    GaussianPivot(a, b, x, n)
    print('\nThe Solution for section 6.2 part 2.a is:')
    print(x, '\n\n-------------------------------------')

    # ------------------------------------------------

    a = array([[5, 1, -6],
               [2, 1, -1],
               [6, 12, 1]], float)

    b = array([7, 8, 9])
    n = len(b)
    GaussianPivot(a, b, x, n)
    print('\nThe Solution for section 6.2 part 2.c is:')
    print(x)
