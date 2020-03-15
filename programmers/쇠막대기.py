def solution(arrangement):
    stack = []
    cnt = 0

    for a, b  in enumerate(arrangement):
        if b == '(':
            stack.append(b)
        elif b == ')' and arrangement[a-1] == '(': # 레이저 완성
            stack.pop()
            cnt += len(stack)
        elif b == ')':
            stack.pop()
            cnt += 1


    return stack, cnt


print(solution('()(((()())(())()))(())'))