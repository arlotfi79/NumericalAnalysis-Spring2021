# using zeros function to create empty array
import numpy as np


def GaussianBackward(n, aug, sol):
    # Gauss Elimination
    for i in range(n):
        if aug[i][i] == 0.0:
            print('Divide by zero!')
            return

        for j in range(i + 1, n):
            m = aug[j][i] / aug[i][i]

            for k in range(n + 1):
                aug[j][k] = aug[j][k] - m * aug[i][k]

    # Back Substitution
    sol[n - 1] = aug[n - 1][n] / aug[n - 1][n - 1]

    for i in range(n - 2, -1, -1):
        sol[i] = aug[i][n]
        for j in range(i + 1, n):
            sol[i] = sol[i] - aug[i][j] * sol[j]

        sol[i] = sol[i] / aug[i][i]


if __name__ == "__main__":
    # number of unknowns
    n = 3
    # for storing augmented matrix
    aug = np.zeros((n, n + 1))
    # for storing solution vector
    sol = np.zeros(n)
    # Reading augmented matrix coefficients
    aug = [[1/4, 1/5, 1/6, 9],
           [1/3, 1/4, 1/5, 8],
           [1/2, 1, 2, 8]]

    GaussianBackward(n, aug, sol)

    # Print solution
    print('Our Solution for Section 6.2 part 2.a is: ')
    for i in range(n):
        print('X%d = %0.2f' % (i+1, sol[i]), end='\t\t')

    aug = [[1/2, 1/4, -1/8, 0],
           [1/3, -1/6, 1/9, 1],
           [1/7, 1/7, 1/10, 2]]

    GaussianBackward(n, aug, sol)

    # Print solution
    print('\n\nOur Solution for Section 6.2 part 2.c is: ')
    for i in range(n):
        print('X%d = %0.2f' % (i + 1, sol[i]), end='\t\t')
