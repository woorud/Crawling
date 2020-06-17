n = int(input())
pole = [list(map(int, input().split())) for i in range(n)]
pole = sorted(pole, key = lambda x : x[0])

dp = [0 for i in range(n)]
dp[0] = 1

for i in range(1, n):
    value = 0
    for j in range(i):
        if pole[i][1] > pole[j][1]:
            value = max(dp[j], value)
    dp[i] = value + 1

print(n-max(dp))