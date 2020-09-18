n, m = map(int, input().split())
h_array = list(map(int, input().split()))

start = 0
end = max(h_array)

res = 0
while start <= end:
    tot = 0
    mid = (start+end)//2
    for i in h_array:
        # 잘랐을 때 떡의 길이 계산
        if i > mid:
            tot += i-mid
    # 떡의 길이가 부족할 경우 더 많이 자르기(왼쪽 부분 탐색)
    if tot < m:
        end = mid - 1
    # 떡의 길이가 넘칠 경우 덜 자르기(오른쪽 부분 탐색)
    else:
        res = mid # 최대한 덜 잘랐을 때가 정답
        start = mid + 1

print(res)