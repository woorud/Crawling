def solution(s):
    res = len(s)
    for i in range(1, len(s)//+1):
        cnt = 1
        x = ''
        prev = s[0:i]
        for j in range(i, len(s), i):
            now = s[j:j+i]
            if prev == now:
                cnt += 1
            else:
                if cnt >= 2:
                    x += str(cnt) + prev

                else:
                    x += prev
                prev = s[j:j + i]
                cnt = 1
        if cnt >= 2:
            x += str(cnt) + prev
        else:
            x += prev

        res = min(len(x), res)
    return res

print(solution("aabbaccc"))