n = int(input())
R_list = [0 for i in range(n)]
G_list = [0 for i in range(n)]
B_list = [0 for i in range(n)]

for i in range(n):
    R, G, B = map(int, input().split())
    R_list[i] = R
    G_list[i] = G
    B_list[i] = B

res = [[0, 0, 0] for i in range(n)]
for i in range(n):
    if i == 0:
        res[i][0] = R_list[i]
        res[i][1] = G_list[i]
        res[i][2] = B_list[i]
    else:
        res[i][0] = min(res[i-1][1], res[i-1][2]) + R_list[i]
        res[i][1] = min(res[i-1][2], res[i-1][0]) + G_list[i]
        res[i][2] = min(res[i-1][0], res[i-1][1]) + B_list[i]

print(min(res[-1]))
