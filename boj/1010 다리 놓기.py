t = int(input())

for i in range(t):
    n, m = map(int, input().split())
    res = 1
    for i in range(1, m+1):
        res *= i
    for i in range(1, m-n+1):
        res //= i
    for i in range(1, n+1):
        res //= i
    print(res)