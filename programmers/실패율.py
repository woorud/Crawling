def solution(N, stages):
    s = sorted(stages)
    p = len(stages)
    stage = {}
    for i in range(1, N+1):
        if i in stages:
            stage[i] = stages.count(i) / p
            p -= stages.count(i)
        else:
            stage[i] = 0
    return sorted(stage, key = lambda x : stage[x], reverse = True)





print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4, [4, 4, 4, 4, 4]))