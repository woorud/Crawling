n, k = map(int, input().split())
item = []
for i in range(n):
    wv = list(map(int, input().split()))
    item.append(wv)
dp = [[0]*(k+1) for i in range(n)]

for i in range(n):
    for j in range(1, k+1):
        w = item[i][0] # i = 1, 4
        v = item[i][1] # i = 1, 8
        if w > j: # j = 1,2,3
            dp[i][j] = dp[i-1][j]
        else: # j = 4,5,6,7
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w]+v)

print(dp[-1][-1])