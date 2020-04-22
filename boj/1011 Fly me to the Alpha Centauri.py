def solution(x, y):
    distance = 0
    cnt = 0
    while x < y:
        distance += 1
        if y - x <= distance:
            cnt += 1
            break
        else:
            x += distance
            y -= distance
            cnt += 2
    return cnt

n = int(input())
for i in range(n):
    x, y = map(int, input().split())
    print(solution(x, y))