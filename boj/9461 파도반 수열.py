dp = [1, 1, 1, 2, 2]
dp.extend(0 for i in range(96))

for i in range(5, 101):
    dp[i] = dp[i-3] + dp[i-2]

n = int(input())
for i in range(n):
    a = int(input())
    print(dp[a-1])