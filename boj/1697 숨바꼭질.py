from collections import deque
max = 100001
n, k = map(int, input().split())
array = [0] * max

def bfs():
    q = deque([n])
    while q:
        now_pos = q.popleft()
        if now_pos == k:
            return array[now_pos]
        for next_pos in (now_pos-1, now_pos+1, now_pos*2):
            if 0 <= next_pos < max and not array[next_pos]: # 범위 내에 있고 방문하지 않았다면
                array[next_pos] = array[now_pos]+1 # 이전 정점 + 1 = 새로운 정점의 최소시간
                q.append(next_pos)

print(bfs())