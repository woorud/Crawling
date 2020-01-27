def solution(n):
    import math
    num = math.sqrt(n)

    if num % 1 == 0:
        return (num+1) * (num+1)
    else:
        return -1

print(solution(121))
print(solution(3))
