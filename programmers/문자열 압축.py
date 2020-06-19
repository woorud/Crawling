def solution(s):
    char_list = []
    res = ''
    if len(s) == 1:
        return 1

    for i in range(1, len(s)//2+1):
        cnt = 1
        tmp = s[:i]
        for j in range(i, len(s), i):
            if tmp == s[j:j+i]:
                cnt += 1
            else:
                if cnt == 1:
                    cnt = ''
                res += str(cnt)+tmp
                tmp = s[j:j+i]
                cnt = 1
        if cnt == 1:
            cnt = ''
        res += str(cnt) + tmp
        char_list.append(len(res))
        res = ''
    return min(char_list)


print(solution("aabbaccc"))
print(solution("ababcdcdababcdcd"))