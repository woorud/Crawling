n = int(input())
for i in range(n):
    par = list(input())
    s = 0

    while len(par) != 0:
        if s < 0:
            break
        tmp = par.pop()
        if tmp == '(':
            s -= 1
        elif tmp == ')':
            s += 1
    if s == 0:
        print('Yes')
    else:
        print('No')