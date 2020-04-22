from collections import deque
n, m = map(int, input().split())
num_list = list(map(int, input().split()))
dq = deque([i for i in range(1, n+1)])
cnt = 0

for i in num_list:
    if i == dq[0]:
        dq.popleft()
        continue
    left = dq.index(i)
    right = len(dq) - left

    if left <= right:
        dq.rotate(-left)
        dq.popleft()
        cnt += left

    else:
        dq.rotate(right)
        dq.popleft()
        cnt += right
print(cnt)