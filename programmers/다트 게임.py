def solution(dartResult):
    dartResult = dartResult.replace('10', 'a')
    dR = list(dartResult)
    score = []

    for i in dR:
        if i.isdigit():
            score.append(int(i))
        elif i == 'a':
            score.append(10)
        elif i.isalpha():
            if i == 'S':
                score[-1] = score[-1] ** 1
            elif i == 'D':
                score[-1] = score[-1] ** 2
            elif i == 'T':
                score[-1] = score[-1] ** 3
        else:
            if i == '#':
                score[-1] = score[-1] * (-1)
            else:
                if len(score) == 1:
                    score[-1] = score[-1] * 2
                else:
                    score[-1] = score[-1] * 2
                    score[-2] = score[-2] * 2

    return sum(score)



print(solution('1S2D*3T'))
print(solution('10S2D*3T'))
print(solution('1S*2T*3S'))
print(solution('1D#2S*3S'))
print(solution('1D2S#10S'))