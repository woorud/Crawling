def solution(s):
    l = 0
    r = 0
    for i in s :
        if i == '(':
            l += 1
        else:
            r += 1
        if l < r:
            return False
    if l == r:
        return True
    else:
        return False


print(solution('()()'))
print(solution('(())()'))
print(solution(')()('))
print(solution('()))((()'))