def solution(participant, completion):
    pd = {}
    for i in participant :
        if i not in pd :
            pd[i] = 1
        else:
            pd[i] += 1

    for i in completion :
        if i in pd:
            pd[i] -= 1

    for i, j in pd.items():
        if j != 0 :
            return i

print(solution(['mislav', 'stanko', 'mislav', 'ana'], ['stanko', 'ana', 'mislav']))