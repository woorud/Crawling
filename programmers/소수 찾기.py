from itertools import permutations
def solution(numbers):
    numlist = []
    for i in range(1, len(numbers)+1):
        p = permutations(numbers, i)
        for j in p:
            numlist.append(int(''.join(j)))


    numlist = set(numlist)

    d = {}
    for i in numlist:
        dv = 0
        for j in range(1, max(numlist) + 1):
            if i % j == 0:
                dv += 1
                d[i] = dv

    l = []
    for a, b in d.items():
        if b == 2:
            l.append(a)


    return len(l)


print(solution('17'))
print(solution('011'))