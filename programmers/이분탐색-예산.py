def solution(budgets, M):
    budgets.sort()
    start = 0
    end = budgets[-1]
    answer = 0

    while start <= end:
        mid = (start + end) // 2
        tmp = []
        for i in budgets:
            if i < mid:
                tmp.append(i)
            else:
                tmp.append(mid)
        if sum(tmp) > M:
            end = mid - 1
        elif sum(tmp) <= M:
            answer = mid
            start = mid + 1
    return answer

print(solution([120, 110, 140, 150], 485))