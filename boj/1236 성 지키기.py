n, m = map(int, input().split())
matrix = [input() for i in range(n)]

row = [0]*n
column = [0]*m

for i in range(n):
    for j in range(m):
        if matrix[i][j] == 'X':
            row[i] = 1
            column[j] = 1

rc = 0
for i in range(n):
    if row[i] == 0:
        rc += 1
cc = 0
for i in range(m):
    if column[i] == 0:
        cc += 1
print(max(rc, cc))