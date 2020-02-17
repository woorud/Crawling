def solution(answers):
    a = [1, 2, 3, 4, 5] * 10000
    b = [2, 1, 2, 3, 2, 4, 2, 5] * 10000
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 10000
    score = [0, 0, 0]

    for i in range(len(answers)):
        if answers[i] == a[i]:
            score[0] += 1
        if answers[i] == b[i]:
            score[1] += 1
        if answers[i] == c[i]:
            score[2] += 1

    answer = []
    m = max(score)
    for i in range(len(score)):
        if score[i] == m:
            answer.append(i+1)

    return answer

print(solution([1,2,3,4,5]))
print(solution([1,3,2,4,2]))