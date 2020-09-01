def solution(s):
    char_list =[]
    res = ''

    if len(s) == 1:
        return 1

    for i in range(1, len(s)//2+1):
        tmp = s[:i]
        n = 1
        for j in range(i, len(s), i):
            if tmp == s[j:j+i]:
                n += 1
            else:
                if n == 1:
                    n = ''
                res += str(n) + tmp
                tmp = s[j:j+i]
                n = 1
        if n == 1:
            n = ''
        res += str(n) + tmp
        char_list.append(res)
        res = ''

    return char_list




print(solution("aabbaccc"))
print(solution("ababcdcdababcdcd"))
print(solution("abcabcdede"))
print(solution("abcabcabcabcdededededede"))
print(solution("xababcdcdababcdcd"))
