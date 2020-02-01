import math #math.round(): 반올림
            #math.ceil(): 올림
            #math.floor(): 내림
            #math.abs(): 절대값
            #math.max,min(): 최대값, 최소값
            #math.pow(): a의 b승과 제곱근
            #math.sqrt(): 제곱근
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