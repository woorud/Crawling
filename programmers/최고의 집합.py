def solution(n, s):
    if n > s:
        return [-1]

    initial = s//n
    res = []
    idx = len(res)-1
    for i in range(n):
        res.append(initial)
    for i in range(s%n):
        res[idx] += 1
        idx -=1
    return res



print(solution(2, 9))
print(solution(2, 1))
print(solution(2, 8))