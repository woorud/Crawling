n = int(input())
array = []
array.append((0, 0, 0, 0))
for _ in range(1, n+1):
    width, height, weight = map(int, input().split())
    array.append((_, width, height, weight))

array.sort(key = lambda x : x[3])

dp = [0] * (n+1)
for i in range(1, n+1):
    for j in range(0, i):
        if array[i][1] > array[j][1]:
            dp[i] = max(dp[i], dp[j]+array[i][2])

max_value = max(dp)
idx = n
res = []

while idx != 0:
    if max_value == dp[idx]:
        res.append(array[idx][0])
        max_value -= array[idx][2]
    idx -= 1

res.reverse()
print(len(res))
[print(i) for i in res]
