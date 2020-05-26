def solution(s):
    res = []

    words = list(s)
    for i in range(len(words)):
        for j in range(i+1, len(words)+1):
            tmp = s[i:j]
            if tmp == tmp[::-1]:
                res.append(tmp)
    m = len(res[0])
    for i in range(1, len(res)):
        if m < len(res[i]):
            m = len(res[i])

    return m

print(solution('abcdcba'))
print(solution('abacde'))