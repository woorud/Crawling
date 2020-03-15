def solution(record):
    d = {}
    for i in record:
        i = i.split(' ')
        if i[0] == 'Enter':
            d[i[1]] = i[2]
        elif i[0] == 'Change':
            d[i[1]] = i[2]

    answer = []
    for i in record:
        rl = i.split(' ')
        cmd = rl[0]

        if cmd == 'Enter':
            answer.append(d[rl[1]] + '님이 들어왔습니다.')
        elif cmd == 'Leave':
            answer.append(d[rl[1]] + '님이 나갔습니다.')

    return answer

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))