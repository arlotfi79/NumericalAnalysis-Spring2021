def nevilleIteration(aboutNode, nodes, lenNodes, Q):
    for i in range(1, lenNodes):
        for j in range(1, i + 1):
            Q[i][j] = ((aboutNode - nodes[i - j]) * Q[i][j - 1] -
                       (aboutNode - nodes[i]) * Q[i - 1][j - 1]) / (nodes[i] - nodes[i - j])

    # Print the result
    print()
    for i in range(lenNodes):
        for j in range(i + 1):
            print('Q[%d][%d] = %.7f \t\t' % (i, j, Q[i][j]),end='')
        print()


if __name__ == "__main__":
    # nodes = 1.0 1.3 1.6 1.9 2.2
    # col1 Q: 0.7651977 0.6200860 0.4554022 0.2818186 0.1103623

    nodes = input('Enter Nodes: ')
    nodes = [float(x) for x in nodes.split()]
    lenNodes = len(nodes)
    temp = input('input col1 Q values: ')
    temp = [float(x) for x in temp.split()]

    Q = []
    for i in range(lenNodes):
        Q.append([0 for _ in range(i+1)])
        Q[i][0] = temp[i]

    nevilleIteration(1.5, nodes, lenNodes, Q)
