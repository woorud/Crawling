n, m = map(int, input().split())
distance = [int(input()) for i in range(n)]
distance = sorted(distance)

start = distance[1] - distance[0]
end = distance[-1] - distance[0]
res = 0

while start <= end :
    mid = (start+end) // 2
    val = distance[0]
    cnt = 1
    for i in range(1, len(distance)):
        if distance[i] >= val + mid:
            val = distance[i]
            cnt += 1
    if cnt >= m:
        start = mid + 1
        res = mid
    else:
        end = mid - 1
print(res)