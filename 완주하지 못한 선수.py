def solution(participant, completion):
    d = {}
    answer = ''
    for i in participant :
        if i in d :
            d[i] += 1
        else:
            d[i] = 1

    for i in completion :
        if i in d:
            d[i] -= 1

    for i in d.keys():
        if d[i] == 1:
            return i

        
print(solution(['leo', 'kiki', 'eden'], ['eden', 'kiki']))
print(solution(['mislav', 'stanko', 'mislav', 'ana'], ['stanko', 'ana', 'mislav']	))