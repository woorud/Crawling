n = int(input())
dp = [0 for i in range(n+1)]
double = [i*i for i in range(1, int(n**0.5)+1)]

for i in range(1, n+1):
    tmp = []
    for j in double:
        if j > i:
            break
        tmp.append(dp[i-j])
    dp[i] = min(tmp) + 1
print(dp[n])
