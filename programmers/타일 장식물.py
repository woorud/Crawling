def solution(n):
    dp = [0] * 81
    dp[0], dp[1], dp[2] = 1, 1, 2

    for i in range(3, 81):
        dp[i] = dp[i-2] + dp[i-1]
    return (dp[n-1] + dp[n-2])*2 + dp[n-1]*2
print(solution(5))
print(solution(6))