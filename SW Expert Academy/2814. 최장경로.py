def dfs(v):





t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    adj = [[] for i in range(n+1)]
    visit = [False for i in range(n+1)]

    for i in range(m):
        x, y = map(int, input().split())
        adj[x].append(y)
        adj[y].append(x)
