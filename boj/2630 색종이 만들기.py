def quad(x, y, n):
    global n, blue, white
    color = matrix[y][n]
    b = False

    for i in range(x, x + n):
        if b:
            break
        for j in range(y, y + n):
            if matrix[j][i] != color:
                quad(x, y, n // 2)
                quad(x + n // 2, y, n // 2)
                quad(x, y + n // 2, n // 2)
                quad(x + n // 2, y + n // 2, n // 2)
                b = True
                break
    if not b:
        if matrix[y][x] == 1:
            blue += 1
        else:
            white += 1


n = int(input())
blue = 0
white = 0
matrix = []
for _ in range(n):
    matirx.append(list(map(int, input().split())))