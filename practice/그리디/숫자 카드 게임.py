n, m = map(int, input().split())
res = 0
for _ in range(n):
    num_list = list(map(int, input().split()))
    m = min(num_list)
    if m > res:
        res = m
print(res)
