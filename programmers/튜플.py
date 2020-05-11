from collections import Counter
def solution(s):
    s = s.split(',')
    l = []
    for i in s:
        tmp = ''
        for j in i:
            if j != '{' and j != '}':
                tmp += j
        l.append(int(tmp))

    dic = Counter(l)
    counter = dic.most_common()
    res = []
    for i in counter:
        res.append(i[0])
    return res

print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))
print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))
print(solution("{{20,111},{111}}"))
print(solution("{{123}}"))
print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"))