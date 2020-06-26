for i in range(10):
    t = int(input())
    f = input()
    w = list(input())
    cnt = 0
    for j in range(len(w)):
        tmp = w[j:j+len(f)]
        if ''.join(tmp) == f:
            cnt += 1
    print('#{} {}'.format(t, cnt))