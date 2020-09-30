n = int(input())
fearness = list(map(int, input().split()))
fearness.sort()

res = 0
cnt = 0
for i in fearness:
    cnt += 1
    if cnt >= i:
        res += 1
        cnt = 0

print(res)