def check_score(question, candidate, s, b):
    strike = 0
    for i in range(len(question)):
        if question[i] == candidate[i]:
            strike += 1
    if s != strike:
        return False

    ball = len(set(question) & set(candidate)) - strike
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

print(solution([[123, 1, 1], [356, 1, 0], [327, 2, 0], [489, 0, 1]]))