for _ in range(10):
    t, num = input().split()
    num_list = []
    for i in num:
        num_list.append(int(i))

    res = []
    for i in num_list:
        if len(res) == 0:
            res.append(i)
        else:
            if res[-1] == i:
                res.pop()
            else:
                res.append(i)

    ans = ''
    for i in res:
        ans += str(i)

    print('#{} {}'.format(_+1, ans))