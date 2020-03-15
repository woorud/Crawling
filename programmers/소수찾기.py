def solution(n):
    d = {}
    for i in range(2, n+1):
        cnt = 0
        for j in range(1, n+1):
            if i % j == 0:
                cnt += 1
                d[i] = cnt
    l = []
    for i in d.items():
        if i[1] == 2:
            l.append(i[0])
    return len(l)

print(solution(5))
print(solution(10))
print(solution(100))