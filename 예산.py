def solution(d, budget):
    d = sorted(d)
    result = 0
    bl = []

    for i in d:
        bl.append(i)
        if sum(bl) < budget:
            result += 1
        elif sum(bl) == budget:
            result = len(bl)
        else:
            continue

    return result

print(solution([2, 2, 3, 3], 10))
print(solution([1, 3, 2, 5, 4], 9))