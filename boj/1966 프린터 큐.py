n = int(input())
for i in range(n):
    s, w = map(int, input().split())
    prior = list(map(int, input().split()))
    p = [(a, b) for a, b in enumerate(prior)]

    cnt = 0
    while True:
        if p[0][1] == max(p, key = lambda x : x[1])[1]:
            cnt += 1
            if p[0][0] == w:
                print(cnt)
                break
            else:
                p.pop(0)
        else:
            p.append(p.pop(0))