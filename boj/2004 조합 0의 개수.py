def five(n):
    ans = 0
    while n != 0:
        n = n // 5
        ans += n
    return ans

def two(n):
    ans = 0
    while n != 0:
        n = n // 2
        ans += n
    return ans

n, m = map(int, input().split())
if m == 0:
    print(0)
else:
    print(min(two(n)-two(m)-two(n-m), five(n)-five(m)-five(n-m)))

