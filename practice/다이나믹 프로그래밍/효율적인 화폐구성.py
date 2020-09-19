n, m = map(int, input().split())
coin = []
for i in range(n):
    coin.append(int(input()))
dp = [10001] * (m+1)

dp[0] = 0
for i in range(n):
    for j in range(coin[i], m+1):
        if dp[j-coin[i]] != 10001:
            dp[j] = min(dp[j], dp[j-coin[i]]+1)

if dp[m] == 10001:
    print(-1)
else:
    print(dp[m])
'''
0 1 2 3 4 5 6 7 8 9 10
0 0 1 1 2 2 2 3 3 3 
'''