def balanced(p):
    tmp = 0
    for i, v in enumerate(p):
        if v == '(':
            tmp += 1
        if v == ')':
            tmp -= 1
        if tmp == 0:
            return i

def is_right(p):
    tmp = []
    for i in p:
        if i == '(':
            tmp.append(i)
        else:
            if len(tmp) == 0:
                return False
            tmp.pop()
    if len(tmp) == 0:
        return True
    return False

def solution(p):
    if len(p) == '' or is_right(p):
        return p

    u = p[:balanced(p)+1]
    v = p[balanced(p)+1:]

    if is_right(u):
        string = solution(v)
        return u + string
    else:
        a = '('
        a += solution(v)
        a += ')'

        u = list(u[1:-1])

        for i in range(len(u)):
            if u[i] == '(':
                u[i] = ')'
            elif u[i] == ')':
                u[i] = '('
        a += ''.join(u)
        return a





print(solution("(()())()"))
print(solution(")("))
print(solution("()))((()"))

