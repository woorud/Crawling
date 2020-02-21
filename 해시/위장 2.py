def solution(clothes):
    cd = {}
    for i in clothes :
        if i[1] not in cd:
            cd[i[1]] = 1
        else:
            cd[i[1]] += 1

    answer = 1
    for i in cd:
        answer *= (cd[i]+1)
    return answer-1

print(solution([['crow_mask', 'face'], ['blue_sunglasses', 'face'], ['smoky_makeup', 'face']]))
print(solution([['yellow_hat', 'headgear'], ['blue_sunglasses', 'eyewear'], ['green_turban', 'headgear']]))