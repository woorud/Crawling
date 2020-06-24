n = int(input())
for i in range(1, n+1):
    i = list(str(i))
    cnt = 0
    for j in i:
        if j == '3' or j == '6' or j == '9':
            cnt += 1
    if cnt == 0:
        print(''.join(i), end = ' ')
    else:
        print('-' * cnt, end = ' ')
