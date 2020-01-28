def solution(n):
    res = []
    for i in str(n):
        res.append(i)

        res.sort()
        res.reverse()


    return  int(''.join(res))


print(solution(118372))