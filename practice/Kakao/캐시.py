def solution(cacheSize, cities):
    if cacheSize == 0:
        return 5 * len(cities)

    cities = [i.lower() for i in cities]

    res = 0
    q = []
    for i in range(len(cities)):
        tmp = cities.pop(0)
        if len(q) != cacheSize:
            if tmp not in q:
                q.append(tmp)
                res += 5
            else:
                q.remove(tmp)
                q.append(tmp)
                res += 1
        else:
            if tmp not in q:
                q.pop(0)
                q.append(tmp)
                res += 5
            else:
                q.remove(tmp)
                q.append(tmp)
                res += 1

    return res
print(solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))
print(solution(3, ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]))
print(solution(2, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]))
print(solution(5, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]))
print(solution(2, ["Jeju", "Pangyo", "NewYork", "newyork"]))
print(solution(0, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))