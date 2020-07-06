def solve(n, x, y):
    global res
    if n == 2:
        if x == c and y == r:
            print(res)
            return
        res += 1
        if x == c and y+1 == r:
            print(res)
            return
        res += 1
        if x+1 == c and y == r:
            print(res)
            return
        res += 1
        if x+1 == c and y+1 == r:
            print(res)
            return
        res += 1
        return
    solve(n/2, x, y)
    solve(n/2, x, y+n / 2)
    solve(n/2, x+n / 2, y)
    solve(n/2, x+n / 2, y+n / 2)

res = 0
N, c, r = map(int, input().split())
solve(2**N, 0, 0)