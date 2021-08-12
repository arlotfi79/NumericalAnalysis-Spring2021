def totalDet(ar):
    if len(ar) == 0:
        return 1
    elif len(ar) == 1:
        return int(ar[0][0])
    elif len(ar) == 2:
        return int((ar[0][0] * ar[1][1]) - (ar[0][1] * ar[1][0]))

    summation = 0
    for j in range(len(ar)):
        coefficient = (-1) ** j
        summation += (coefficient * ar[0][j] * totalDet(squareDet(ar, 0, j)))
    return summation


def squareDet(array, x, y):
    return [row[:y] + row[y + 1:] for row in (array[:x] + array[x + 1:])]


if __name__ == "__main__":
    a = int(input('Number of Rows: '))
    matrix = []
    for i in range(a):
        matrix.append(list(map(int, input().split())))
    print(totalDet(matrix))
