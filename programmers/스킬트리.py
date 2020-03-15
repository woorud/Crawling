def solution(skill, skill_trees):
    l = []
    for i in skill_trees:
        idx = []
        for j in skill:
            if j in i:
                idx.append(i.index(j))
            else:
                idx.append(27)
        l.append(idx)

    s = 0
    for i in l:
        if i == sorted(i):
            s += 1


    return s

print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))