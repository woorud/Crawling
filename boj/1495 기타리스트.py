n, s, m = map(int, input().split())
array = list(map(int, input().split()))

v = [[0]*(m+1) for i in range(n+1)]
v[0][s] = 1
for i in range(1, n+1):
    for j in range(m+1):
        if v[i-1][j] == 0:
            continue
        if j - array[i-1] >= 0:
            v[i][j-array[i-1]] = 1
        if j + array[i-1] <= m:
            v[i][j+array[i-1]] = 1
print(v)
res = -1
for i in range(m, -1, -1):
    if v[n][i] == 1:
        res = i
        break
print(res)