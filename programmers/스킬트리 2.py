def solution(skill, skill_trees):
    cnt = 0
    for skills in skill_trees:
        skill_list = list(skill)

        for i in skills:
            if i in skill:
                if i != skill_list.pop(0):
                    break
        else:
            cnt += 1
    return cnt





print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))