import sys
for i in range(10):
    t = int(input())
    matrix = []
    for j in range(100):
        matrix.append(list(map(int, input().split())))

    res = []
    for a in range(100):
        v1 = 0
        v2 = 0
        v3 = 0
        v4 = 0
        for b in range(100):
            v1 += matrix[a][b]
            v2 += matrix[b][a]
        v3 += matrix[a][a]
        v4 += matrix[a][99-a]
        res.append(v1)
        res.append(v2)
        res.append(v3)
        res.append(v4)

    print('#{} {}'.format(t, max(res)))