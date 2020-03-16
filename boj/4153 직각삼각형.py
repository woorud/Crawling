while True:
    a, b, c = list(map(int,input().split()))
    l = [a, b, c]
    l.sort()
    if a == 0 and b == 0 and c == 0:
        break

    if l[0]**2 + l[1]**2 == l[2]**2:
        print('right')
    else:
        print('wrong')