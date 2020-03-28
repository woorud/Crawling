def check_score(sc, cd, s, b):
    strike = 0
    for i in range(len(sc)):
        if sc[i] == cd[i]:
            strike += 1
    if s != strike:
        return False

    ball = len(set(sc)&set(cd)) - strike
    if b != ball:
        return False
    return True

from itertools import permutations
def solution(baseball):
    l = list(permutations([1,2,3,4,5,6,7,8,9], 3))

    for i in baseball:
        for j in l[:]:
             if check_score([int(i) for i in list(str(i[0]))], j, i[1], i[2]) == False:
                 l.remove(j)
    return len(l)

n = int(input())
baseball = []
for i in range(n):
    a, b, c = list(map(int, input().split()))
    baseball += [[a, b, c]]
print(solution(baseball))