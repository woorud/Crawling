while True:
    string = input()
    stack = []
    check = True

    if string == '.':
        break

    for i in string:
        if i == '(' or i == '[':
            stack.append(i)
        elif i == ']':
            if len(stack) == 0:
                check = False
                break
            remove_data = stack.pop()
            if remove_data != '[':
                check = False
                break
        elif i == ')':
            if len(stack) == 0:
                check = False
                break
            remove_data = stack.pop()
            if remove_data != '(':
                check = False
                break
    if len(stack) != 0:
        check = False

    if check:
        print('yes')
    else:
        print('no')