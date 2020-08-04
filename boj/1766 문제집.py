'''
위상정렬 알고리즘
1. 진입차수가 0인 정점을 큐에 삽입
2. 큐에서 원소를 꺼내 해당 원소와 간선을 제거
3. 제거 이후에 진입 차수가 0이 된 정점을 큐에 삽입
4. 큐가 빌 때까지 2~3 과정을 반복
-> 모든 원소를 방문하기 전에 큐가 빈다면 사이클이 존재, 위상정렬은 사이클이 존재하면 안된다.
'''

import heapq
n, m = map(int, input().split())
array = [[] for i in range(n+1)]
indegree = [0] * (n+1)

heap = []
for _ in range(m):
    x, y = map(int, input().split())
    array[x].append(y)
    indegree[y] += 1

for i in range(1, n+1):
    if indegree[i] == 0:
        heapq.heappush(heap, i)

res = []
while heap:
    data = heapq.heappop(heap)
    res.append(data)
    for y in array[data]:
        indegree[y] -= 1
        if indegree[y] == 0:
            heapq.heappush(heap, y)
for i in res:
    print(i, end = ' ')