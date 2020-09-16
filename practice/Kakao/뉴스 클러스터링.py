def solution(str1, str2):
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    s1 = []
    str1 = str1.upper()
    for i in range(len(str1)-1):
        tmp = ''
        for j in str1[i:i+2]:
            if j in alpha:
                tmp += j
        if len(tmp) == 2:
            s1.append(tmp)

    s2 = []
    str2 = str2.upper()
    for i in range(len(str2)-1):
        tmp = ''
        for j in str2[i:i+2]:
            if j in alpha:
                tmp += j
        if len(tmp) == 2:
            s2.append(tmp)


    s = len(s1) + len(s2)
    intersection = 0
    for i in s1:
        if i in s2:
            s2.remove(i)
            intersection += 1
    if s == 0:
        return 65536
    return int((intersection/(s-intersection))*65536)


print(solution("FRANCE", "french"))
print(solution("handshake", "shake hands"))
print(solution("aa1+aa2", "AAAA12"))
print(solution("E=M*C^2", "e=m*c^2"))