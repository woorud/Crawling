def solution(bridge_length, weight, truck_weights):
    passing = [0] * bridge_length
    sec = 0
    while passing:
        sec += 1
        passing.pop(0)

        if truck_weights:
            if sum(passing) + truck_weights[0] <= weight :
                passing.append(truck_weights.pop(0))
            else:
                passing.append(0)
    return sec
print(solution(2, 10, [7, 4, 5, 6]))
print(solution(100, 100, [10]))