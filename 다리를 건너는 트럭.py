def solution(bridge_length, weight, truck_weights):
    passing = [0] * bridge_length
    sec = 0
    stay = 0

    while truck_weights:
        sec += 1
        out = passing.pop(0)
        if out != 0:
            stay -= out

        if stay + truck_weights[0] <= weight:
            ing = truck_weights.pop(0)
            passing.append(ing)
            if ing != 0:
                stay += ing
        else:
            passing.append(0)

    return sec + bridge_length

print(solution(2, 10, [7, 4, 5, 6]))
print(solution(100, 100, [10]))