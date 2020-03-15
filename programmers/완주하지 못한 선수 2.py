from collections import Counter

def solution(participant, completion):
    participant.sort()
    completion.sort()

    a = Counter(participant)
    b = Counter(completion)
    c = a-b

    for i in c.keys():
        return i

print(solution(['leo', 'kiki', 'eden'], ['eden', 'kiki']))
print(solution(['mislav', 'stanko', 'mislav', 'ana'], ['stanko', 'ana', 'mislav']))