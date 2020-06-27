for i in range(10):
    t = int(input())
    n, m = map(int, input().split())
    res = 1
    for j in range(m):
        res *= n
    print('#{} {}'.format(t, res))