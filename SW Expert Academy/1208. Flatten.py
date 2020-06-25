for i in range(10):
    t = int(input())
    box = list(map(int, input().split()))

    while t:
        box.sort()
        n = box.pop(0)
        m = box.pop()
        n = n+1
        m = m-1
        box.append(n)
        box.append(m)
        t -= 1

    res = box[-1] - box[0]

    print('#{} {}'.format(i+1, res+1))