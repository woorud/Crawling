for i in range(10):
    t = int(input())
    case = list(map(int, input().split()))

    res = 0
    for j in range(2, len(case)-2):
        around = max([case[j-2], case[j-1], case[j+2], case[j+1]])
        if case[j] > around:
            res += case[j] - around

    print('#{} {}'.format(i+1, res))