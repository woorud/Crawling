def solution(A,B):
    l = []
    for a, b in zip(sorted(A), sorted(B, reverse = True)):
        l.append(a*b)
    return sum(l)

print(solution([1, 4, 2], [5, 4, 4]))
print(solution([1, 2], [3, 4]))






