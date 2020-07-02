t = int(input())
for _ in range(t):
    s = int(input())
    matrix = []
    for i in range(s):
        matrix.append(list(input()))

    res = 0
    a = s // 2
    b = s // 2 + 1
    for i in range(s//2):
        for j in matrix[i][a:b]:
            res += int(j)
        a -= 1
        b += 1
    for i in range(s//2, s):
        for j in matrix[i][a:b]:
            res += int(j)
        a += 1
        b -= 1

    print('#{} {}'.format(_+1, res))