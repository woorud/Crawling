for _ in range(10):
    t = int(input())
    matrix = []
    for i in range(t):
        matrix.append(list(map(int, input().split())))
    new_matrix = []
    for i in range(100):
        tmp = []
        for j in range(100):
            tmp.append(matrix[j][i])
        new_matrix.append(tmp)

    res = 0
    tf = False
    for i in new_matrix:
        for j in i:
            if j == 1:
                tf = True
            if j == 2 and tf == True:
                res += 1
                tf = False
        tf = False
    print('#{} {}'.format(_+1, res))