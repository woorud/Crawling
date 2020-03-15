def solution(clothes):
    tp = {}
    for c, t in clothes:
        if t not in tp :
            tp[t] = 2
        else:
            tp[t] += 1

    cnt = 1
    for i in tp.values():
        cnt *= i
    return cnt - 1

print(solution([['yellow_hat', 'headgear'], ['blue_sunglasses', 'eyewear'], ['green_turban', 'headgear']]))