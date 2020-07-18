def dfs(cnt, res):
    global n, b
    if res >= b:
        ans.append(res)
    if cnt >= n:
        return
    dfs(cnt+1, res)
    dfs(cnt+1, res+h[cnt])

t = int(input())
for _ in range(1, 1+t):
    n, b = map(int, input().split())
    h = sorted(list(map(int, input().split())))
    ans = []
    dfs(0,0)
    print('#{} {}'.format(_, sorted(ans)[0]-b))