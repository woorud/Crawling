n, m = map(int, input().split()) # 3, 2
a = []
for i in range(n):
    a.append(list(map(int, input().split())))
m, k = map(int, input().split()) # 2, 3
b = []
for i in range(m):
    b.append(list(map(int, input().split())))

res = [[0 for i in range(k)] for i in range(n)]
for o in range(n):
    for t in range(k):
        for h in range(m):
            res[o][t] += a[o][h] * b[h][t]

for i in res:
    for j in i:
        print(j, end = ' ')
    print()