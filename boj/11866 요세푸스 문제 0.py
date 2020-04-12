from collections import deque
n, k = map(int, input().split())

dq = deque()
for i in range(1, n+1):
    dq.append(i)
res = []
while dq:
    for i in range(k-1):
        dq.append(dq[0])
        dq.popleft()
    res.append(dq.popleft())

print('<' + ', '.join(map(str, res)) + '>')