def solution(answers):
    sd = {1 : [1, 2, 3, 4, 5], 2 : [2, 1, 2, 3, 2, 4, 2, 5], 3 : [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]}
    scores = []

    for i in sd:
        score = 0
        for idx, answer in enumerate(answers):
            if answer == sd[i][idx % len(sd[i])]:
                score += 1
        scores.append((score, i))
    scores.sort(reverse = True)

    answer = []
    sl = []
    for i in range(len(scores)):
        sl.append(scores[i][0])
        m = max(sl)
        if scores[i][0] == m :
            answer.append(scores[i][1])

    return sorted(answer)

print(solution([1,2,3,4,5]))
print(solution([1,3,2,4,2]))
