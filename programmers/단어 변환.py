def solution(begin, target, words):
    l = [begin]
    if target not in words:
        return 0

    res = 0
    while len(words) != 0:
        for i in l:
            tmp = []
            for word in words:
                cnt = 0
                for k in range(len(i)):
                    if i[k] != word[k]:
                        cnt += 1
                    if cnt == 2:
                        break
                if cnt == 1:
                    tmp.append(word)
                    words.remove(word)
        res += 1
        if target in tmp:
            return res
        else:
            l = tmp
    return 0


print(solution('hit', 'cog', ['hot', 'dot', 'dog', 'lot', 'log', 'cog']))