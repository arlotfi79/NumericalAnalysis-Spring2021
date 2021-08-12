import numpy as np
import matplotlib.pyplot as plt


# Computing Coefficients
def Cofficients(n, x, a):
    h = np.zeros(n)
    for i in range(n):
        h[i] = x[i + 1] - x[i]

    alpha = np.zeros(n)
    for i in range(1, n):
        alpha[i] = (3 / h[i]) * (a[i + 1] - a[i]) - (3 / h[i - 1]) * (a[i] - a[i - 1])

    l = np.zeros(n + 1)
    mio = np.zeros(n + 1)
    z = np.zeros(n + 1)
    c = np.zeros(n + 1)
    b = np.zeros(n)
    d = np.zeros(n)

    l[0] = 1
    z[0] = 0
    mio[0] = 0

    for i in range(1, n):
        l[i] = 2 * (x[i + 1] - x[i - 1]) - h[i - 1] * mio[i - 1]
        mio[i] = h[i] / l[i]
        z[i] = (alpha[i] - h[i - 1] * z[i - 1]) / l[i]

    l[n] = 1
    z[n] = 0
    c[n] = 0

    for j in range(n - 1, -1, -1):
        c[j] = z[j] - mio[j] * c[j + 1]
        b[j] = ((a[j + 1] - a[j]) / h[j]) - (h[j] * (c[j + 1] + 2 * c[j]) / 3)
        d[j] = (c[j + 1] - c[j]) / (3 * h[j])

    return a, b, c, d


# Computing Spline Function
def Spline(j, x):
    return A[j] + B[j] * (x - Xs[j]) + C[j] * ((x - Xs[j]) ** 2) + D[j] * ((x - Xs[j]) ** 3)


def createSplineFunction(include):
    if not include:
        for i in range(len(X_S)):
            if -2 <= X_S[i] < -1:
                Y_S[i] = Spline(0, X_S[i])
            elif -1 <= X_S[i] < 1:
                Y_S[i] = Spline(1, X_S[i])
            elif 1 <= X_S[i] < 2:
                Y_S[i] = Spline(2, X_S[i])
    else:
        for i in range(len(X_S)):
            if -2 <= X_S[i] < -1:
                Y_S[i] = Spline(0, X_S[i])
            elif -1 <= X_S[i] < 0:
                Y_S[i] = Spline(1, X_S[i])
            elif 0 <= X_S[i] < 1:
                Y_S[i] = Spline(2, X_S[i])
            elif 1 <= X_S[i] < 2:
                Y_S[i] = Spline(3, X_S[i])


if __name__ == "__main__":
    # initializing
    Xs = np.array(
        [-2, -1, 1, 2])
    Ys = np.array(
        [1 / (1 + x ** 2) for x in Xs])

    # finding coefficients
    A, B, C, D = Cofficients(len(Xs) - 1, Xs, Ys)

    # making Spline
    X_S = np.arange(Xs[0], Xs[len(Xs) - 1], 0.01)
    Y_S = np.zeros(len(X_S))
    createSplineFunction(False)

    # ---------------------------------------
    # Original
    X = np.arange(-2, 2, 0.01)
    Y = 1 / (1 + X ** 2)
    plt.plot(X, Y, label="Original", color="blue")

    # Spline
    plt.plot(X_S, Y_S, label="Spline", color="red", linestyle='-.')

    # naming the x axis
    plt.xlabel('x - axis')
    # naming the y axis
    plt.ylabel('y - axis')
    # giving a title to my graph
    # plt.title('Using 5 nodes to construct the Spline (Including x = 0)')

    # show a legend on the plot
    plt.legend()
    # plt.show()
    plt.savefig('x.png')
