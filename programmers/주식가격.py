def solution(prices):
    sl = []
    for i in range(len(prices)):
        sec = 0
        for j in range(i+1, len(prices)):
            if prices[i] <= prices[j]:
                sec += 1
            else:
                sec += 1
                break
        sl.append(sec)
    return sl
print(solution([1, 2, 3, 2, 3]))