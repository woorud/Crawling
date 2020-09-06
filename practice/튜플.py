def solution(s):
    tmp = []
    for i in s:
        if i != '{' and i != '}':
            tmp.append(i)

    tmp = ''.join(tmp).split(',')

    ans = {}
    for i in tmp:
        k = int(i)
        if k not in ans:
            ans[k] = 1
        else:
            ans[k] += 1

    answer = sorted(ans.items(), key = lambda x : x[1], reverse = True)

    res = []
    for i in answer:
        res.append(i[0])

    return res


print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))
print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))
print(solution("{{20,111},{111}}"))
print(solution("{{123}}"))
print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"))
