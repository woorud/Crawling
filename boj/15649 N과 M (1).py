n, m = map(int, input().split())
check = [False for i in range(n+1)]
res = [0 for i in range(m)]

def solution(index, n, m):
    if index == m:
        for i in range(m):
            print(res[i], end = ' ')
        print()
        return

    for i in range(1, n+1):
        if check[i]:
            continue
        check[i] = True
        res[index] = i
        solution(index+1, n, m)
        check[i] = False

solution(0, n, m)