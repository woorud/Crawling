n = input()

if '0' not in n:
    print(-1)
else:
    sum_digit = 0
    for i in n:
        sum_digit += int(i)

    if sum_digit % 3 != 0:
        print(-1)
    else:
        for i in sorted(n ,reverse = True):
            print(i, end = '')