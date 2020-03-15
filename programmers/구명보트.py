from collections import deque
def solution(people, limit):
    people.sort()
    people = deque(people)

    cnt = 0
    while people:
        if len(people) == 1:
            cnt += 1
            break

        elif people[0] + people[-1] <= limit:
            people.popleft()
            people.pop()
            cnt += 1

        else:
            people.pop()
            cnt += 1

    return cnt


print(solution([70, 50, 80, 50], 100))