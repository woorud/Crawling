def solution(str1, str2):
    str1 = list(str1.lower())
    str2 = list(str2.lower())
    alpha = 'abcdefghijklmnopqrstuvwxyz'

    fl = []
    for i in range(1, len(str1)):
        if str1[i-1] in alpha and str1[i] in alpha:
            fl.append(str1[i-1] + str1[i])
    sl = []
    for i in range(1, len(str2)):
        if str2[i-1] in alpha and str2[i] in alpha:
            sl.append(str2[i-1] + str2[i])

    summation = len(fl) + len(sl)
    intersection = 0
    for i in sl:
        if i in fl:
            fl.remove(i)
            intersection += 1
    if summation == 0:
        return 65536
    else:
        return int(intersection / (summation - intersection) * 65535)


print(solution('FRANCE', 'french'))
print(solution('handshake', 'shake hands'))
print(solution('aa1+aa2', 'AAAA12'))