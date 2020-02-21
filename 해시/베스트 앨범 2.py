def solution(genres, plays):
    gd = {}
    for i in range(len(genres)):
        if genres[i] not in gd:
            gd[genres[i]] = plays[i]
        else:
            gd[genres[i]] += plays[i]
    gd = sorted(gd.items(), key = lambda x : x[1], reverse = True)

    pd = {}
    for a, (b, c) in zip(genres, enumerate(plays)):
        if a not in pd:
            pd[a] = [(c, b)]
        else:
            pd[a] += [(c, b)]

    answer = []
    for (gr, tp) in gd:
        pd[gr] = sorted(pd[gr], key = lambda x : (-x[0], x[1])) # '-' 를 붙이면 내림차순으로 정렬이 됨.
        for play, idx in pd[gr][:2]:
            answer.append(idx)
    return answer

print(solution(['classic', 'pop', 'classic', 'classic', 'pop'], [500, 600, 150, 800, 2500]))