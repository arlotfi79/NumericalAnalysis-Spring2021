def bisection(func, maxIteration, TOL, start, end):

    startValue = func(start)

    for i in range(maxIteration):
        current = start + (end - start)/2
        currentValue = func(current)
        print('#startPoint: %f \t #endPoint: %f \t #startValue: %f \t #endValue: %f' %
              (start, end, startValue, currentValue))

        if currentValue == 0 or (end - start)/2 <= TOL:
            print('\n#number of iterations -->', i)
            return current

        elif startValue * currentValue > 0:
            start = current
            startValue = currentValue
        else:
            end = current


def function(x):
    return x - (35)**(1/2)


if __name__ == "__main__":
    print('#Result --> %.5f' % bisection(function, 100, 10**(-5), 5, 6))
