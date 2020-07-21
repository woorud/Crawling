t = int(input())
for _ in range(1, t+1):
    n = int(input())
    matrix = [[0]*n for i in range(n)]
    r, c, num, dir = 0, -1, 0, 1
    cnt = n

    while cnt:
        for i in range(cnt):
            num += 1
            c += dir
            matrix[r][c] = num
        cnt -= 1

        for i in range(cnt):
            num += 1
            r += dir
            matrix[r][c] = num
        dir *= -1
    print('#{}'.format(_))
    for i in matrix:
        for j in i:
            print(j, end = ' ')
        print()