t = int(input())
for _ in range(1, t+1):
    n = int(input())
    income = list(map(int, input().split()))
    avg = sum(income) / n
    cnt = 0
    for i in income:
        if i <= avg:
            cnt += 1
    print('#{} {}'.format(_, cnt))