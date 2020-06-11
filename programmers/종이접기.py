def solution(n):
    res = [0]

    for i in range(n-1):
        tmp = []
        for j in range(len(res)):
            if res[j] == 0:
                tmp.append(1)
            elif res[j] == 1:
                tmp.append(0)
        tmp.reverse()
        res = res + [0] + tmp


    return res

print(solution(1))
print(solution(2))
print(solution(3))
print(solution(4))