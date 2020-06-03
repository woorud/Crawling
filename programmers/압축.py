def solution(msg):
    alphabet = 'ABCDEFGHIZKLMNOPQRSTUVWXYZ'
    d = {}
    for i, a in enumerate(alphabet):
        d[a] = i+1

    answer = []
    while True:
        if msg in d:
            answer.append(d[msg])
            break
        for i in range(1, len(msg)+1):
            if msg[0:i] not in d:
                answer.append(d[msg[0:i-1]])
                d[msg[0:i]] = len(d)+1
                msg = msg[i-1:]
                break

    return answer


print(solution('KAKAO'))
print(solution('TOBEORNOTTOBEORTOBEORNOT'))
print(solution('ABABABABABABABAB'))