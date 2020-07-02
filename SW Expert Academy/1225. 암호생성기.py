for i in range(10):
    t = int(input())
    num_list = list(map(int, input().split()))
    num = [1, 2, 3, 4, 5]

    while True:
        a = num_list.pop(0)
        b = num.pop(0)
        num_list.append(a-b)
        num.append(b)

        if num_list[-1] <= 0:
            num_list[-1] = 0
            break

    res = ''
    for j in num_list:
        res += str(j) + ' '
    print('#{} {}'.format(t, res[:-1]))

