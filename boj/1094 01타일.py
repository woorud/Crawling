dp = []
for i in range(1000001):
    dp.append(0)
dp[1], dp[2], dp[3], dp[4] = 1, 2, 3, 5

for i in range(5, 1000001):
    dp[i] = (dp[i-1] + dp[i-2]) % 15746

n = int(input())
print(dp[n])