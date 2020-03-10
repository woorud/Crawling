def solution(bridge_length, weight, truck_weights):
    passing = [0] * bridge_length
    sec = 0
    sq = 0

    while truck_weights :
        sec += 1
        x = passing.pop(0)
        if x != 0:
            sq -= x

        if truck_weights:
            if sq + truck_weights[0] <= weight:
                a = truck_weights.pop(0)
                passing.append(a)
                sq += a
            else:
                passing.append(0)


    return sec + bridge_length
print(solution(2, 10, [7, 4, 5, 6]))
print(solution(100, 100, [10]))