def solution(cacheSize, cities):
    city = []
    for i in cities:
        i = i.lower()
        city.append(i)

    time = 0
    db = []
    if cacheSize != 0 :
        for i in city:
            if i not in db:
                if len(db) < cacheSize :
                    db.append(i)
                    time += 5
                else:
                    db.pop(0)
                    db.append(i)
                    time += 5
            else:
                time += 1
                idx = db.index(i)
                db.pop(idx)
                db.append(i)
    else:
        time = len(city) * 5

    return time

print(solution(2, ['Jeju', 'Pangyo', 'NewYork', 'newyork']))
print(solution(0, ['Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA']))
print(solution(3, ['Jeju', 'Pangyo', 'Seoul', 'Jeju', 'Pangyo', 'Seoul', 'Jeju', 'Pangyo', 'Seoul']))