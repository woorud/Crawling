n, k = map(int, input().split())
c = []
for i in range(n):
    coin = int(input())
    c.append(coin)

cnt = 0
for i in range(len(c)-1, -1, -1):
    if k == 0:
        break
    if c[i] > k:
        continue
    cnt += k//c[i]
    k %= c[i]
print(cnt)