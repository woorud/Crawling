from itertools import permutations as per

def prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def solution(numbers):
    nl = []
    for i in range(1, len(numbers)+1):
        x = per(numbers, i)
        for j in x:
            nl.append(int(''.join(j)))
    nl = set(nl)

    cnt = 0
    for i in nl:
        if i != 0 and i != 1:
            if prime(i) == True:
                cnt += 1
    return cnt


print(solution('17'))
print(solution('011'))