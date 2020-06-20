from itertools import permutations
def match(user_set, banned_set):
    for i in range(len(user_set)):
        if len(user_set[i]) != len(banned_set[i]):
            return False
        for j in range(len(user_set[i])):
            if banned_set[i][j] == '*':
                continue
            if user_set[i][j] != banned_set[i][j]:
                return False
    return True

def solution(user_id, banned_id):
    res = []
    for i in permutations(user_id, len(banned_id)):
        if match(i, banned_id):
            i = set(i)
            if i not in res:
                res.append(i)
    return len(res)

print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"]))
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"]))
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"]))