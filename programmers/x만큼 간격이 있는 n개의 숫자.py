def solution(x, n):
    answer = []
    a = 1
    while True:
        answer.append(x*a)
        a += 1
        if len(answer) == n:
            break
    return answer



print(solution(2,5))
print(solution(-4,2))