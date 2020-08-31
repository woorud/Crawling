def solution(skill, skill_trees):
    answer = 0
    for i in skill_trees:
        tmp = []
        for j in i:
            if j in skill:
                tmp.append(j)
        res = ''.join(tmp)
        if res == skill[0:len(res)]:
            answer += 1
    return answer


print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))