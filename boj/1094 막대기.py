n = int(input())
stick = [64, 32, 16, 8, 4, 2, 1]
cnt = 0

if n in stick:
    print(1)
else:
    for i in stick:
        if n >= i:
            n -= i
            cnt += 1
    print(cnt)