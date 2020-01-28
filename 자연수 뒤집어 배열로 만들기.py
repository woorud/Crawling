def solution(n):
    res = []
    for i in str(n):
        res.append(i)
    res.reverse()
    return list(map(int, res))


print(solution(12345))