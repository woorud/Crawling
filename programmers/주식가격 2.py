from collections import deque
def solution(prices):
    prices = deque(prices)
    secl = []

    while prices:
        sec = 0
        x = prices.popleft()

        for i in prices:
            if x > i :
                sec += 1
                break
            else:
                sec += 1
        secl.append(sec)
    return secl

print(solution([1, 2, 3, 2, 3]))