def solution(priorities, location):
    prlist = []
    for idx, p in enumerate(priorities):
        prlist.append((idx, p))

    q = []
    while prlist:
        pi = prlist.pop(0)
        pr = pi[1]

        pl = []
        for i, p in prlist:
            pl.append(p)
            maxp = max(pl)

        if pr >= maxp:
            q.append(pi)
        else:
            prlist.append(pi)

    for a, b in enumerate(q):
        if b[0] == location :
            return a+1


print(solution([2, 1, 3, 2], 2))
print(solution([1, 1, 9, 1, 1, 1], 0))