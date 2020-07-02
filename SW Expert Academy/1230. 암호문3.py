for _ in range(10):
    n = int(input())
    code = list(map(int, input().split()))
    c = int(input())
    func = list(input().split(' '))

    def I(x, y, s):
        for i in range(y):
            code.insert(x+1, s[i])
            x += 1

    def D(x, y):
        for i in range(y):
            del code[x+1]
            x += 1

    def A(y, s):
        for i in range(y):
            code.append(s[i])

    for i in range(len(func)):
        if func[i] == 'I':
            x = int(func[i+1])
            y = int(func[i+2])
            s = list(map(int, func[i+3:i+3+y]))
            I(x, y, s)

        elif func[i] == 'D':
            x = int(func[i+1])
            y = int(func[i+2])
            D(x, y)

        elif func[i] == 'A':
            y = int(func[i+1])
            s = list(map(int, func[i+2:i+2+y]))
            A(y, s)

    res = ''
    for i in code[1:11]:
        res += str(i) + ' '
    print('#{} {}'.format(_+1, res))