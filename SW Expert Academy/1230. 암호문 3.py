for _ in range(1, 11):
    first = int(input())
    second = input().split()
    third = int(input())
    fourth = input().split()

    for i in range(len(fourth)):
        if fourth[i] == 'I':
            x, y = map(int, fourth[i + 1: i + 3])
            s = list(fourth[i + 3: y + i + 3])
            second[x:x] = s[:]

        elif fourth[i] == 'D':
            x, y = map(int, fourth[i + 1: i + 3])
            s = x + 1
            for j in range(y):
                del second[x]

        elif fourth[i] == 'A':
            y = int(fourth[i+1])
            s = list(fourth[i+2 : y+i+2])
            for i in s:
                second.append(i)
    res = ' '.join(second[:10])
    print('#{} {}'.format(_, res))
