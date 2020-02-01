import math
def solution(progresses, speeds):

    d = []
    for i in range(len(progresses)):
        rp = 100 - progresses[i]
        rd = rp / speeds[i]
        d.append(math.ceil(rd))
    for i in range(1, len(d)):
        if d[i-1] > d[i]:
            d[i] = d[i-1]
    cnt = 1
    answer = []
    for i in range(1, len(d)):
        if d[i-1] >= d[i]:
            cnt += 1
        else:
            answer.append(cnt)
            cnt = 1
    answer.append(cnt)
    return answer


print(solution([93,30,55], [1,30,5]))