n, m = map(int, input().split())
graph = [list(map(int, input())) for i in range(n)]

# dfs로 특정한 노드를 방문한 뒤, 연결된 모든 노드들도 방문
def dfs(x, y):
    # 주어진 범위에서 벗어나는 경우에는 종료
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    # 현재 노드를 방문하지 않았다면
    if graph[x][y] == 0:
        # 해당 노드 방문처리
        graph[x][y] = 1
        # 상, 하, 좌, 우의 위치도 모두 재귀적으로 호출
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True
    return False

cnt= 0
for i in range(n):
    for j in range(m):
        if dfs(i, j):
            cnt += 1
print(cnt)