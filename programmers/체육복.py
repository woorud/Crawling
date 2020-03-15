def solution(n, lost, reserve):
    rl = []
    for i in reserve:
        if i not in lost:
            rl.append(i)
    ll = []
    for i in lost:
        if i not in reserve:
            ll.append(i)

    for i in rl:
        x = i - 1
        y = i + 1
        if x in ll:
            ll.remove(x)
        elif y in ll:
            ll.remove(y)

    return n - len(ll)


print(solution(5, [2, 4], [1, 3, 5]))
print(solution(5, [2, 4], [3]))
print(solution(3, [3], [1]))