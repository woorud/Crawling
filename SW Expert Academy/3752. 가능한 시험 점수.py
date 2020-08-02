t = int(input())
for _ in range(1, t+1):
    n = int(input())
    scorelist = list(map(int, input().split()))
    possible = set([0])
    for i in scorelist:
        num = set()
        for j in possible:
            num.add(i+j)
        possible = set(list(possible) + list(num))
    print('#{} {}'.format(_, len(possible)))