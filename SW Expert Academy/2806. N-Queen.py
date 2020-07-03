def diagnol(idx, c): # 대각선 위치 확인
    for i in range(idx):
        if idx-i == abs(c-map[i]): # 행 - 열의 절대값이 같으면 대각선에 위치
            return True
    return False

def dfs(idx):
    if idx == N:
        global cnt
        cnt += 1
        return
    for i in range(N):
        if visited[i]:
            continue
        if diagnol(idx, i):
            continue
        visited[i] = 1
        map[idx] = i
        dfs(idx+1)
        visited[i] = 0


t = int(input())
for _ in range(t):
    N = int(input())
    map = [0 for i in range(N)]
    visited = [0 for i in range(N)]
    cnt = 0
    dfs(0)
    print('#{} {}'.format(_+1, cnt))