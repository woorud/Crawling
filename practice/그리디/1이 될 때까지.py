n, k = map(int, input().split())

cnt = 0

# n이 k 이상이라면 k로 나누기
while n >= k:
    # n이 k로 나누어지지 않을 때 1 빼기
    while n % k != 0:
        n -= 1
        cnt += 1
    n //= k
    cnt += 1

# 마지막 남은 수에서 1 빼기
while n > 1:
    n -= 1
    cnt += 1
print(cnt)