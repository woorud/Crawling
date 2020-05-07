n = int(input())
wine_list = [int(input()) for x in range(n)]

dp = [0]
dp.append(wine_list[0])
if (n > 1):
    dp.append(wine_list[0] + wine_list[1])


for i in range(3, n + 1):
    c1 = wine_list[i - 1] + dp[i - 2]
    c2 = wine_list[i - 1] + wine_list[i - 2] + dp[i - 3]
    c3 = dp[i - 1]
    max_value = max(c1, c2, c3)
    dp.append(max_value)

print(dp[n])