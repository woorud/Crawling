t = int(input())
for i in range(t):
    n = int(input())
    value = list(map(int, input().split()))[::-1]
    res = 0
    max = value[0]

    for j in range(1, n):
        if max > value[j]:
            res += max - value[j]
        else:
            max = value[j]

    print('#{} {}'.format(i+1, res))