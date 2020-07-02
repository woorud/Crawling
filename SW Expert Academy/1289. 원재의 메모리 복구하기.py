t = int(input())
for _ in range(t):
    code = list(input())
    iv = ['0'] * len(code)
    cnt = 0
    for i in range(len(code)):
        if iv[i] != code[i]:
            for j in range(len(iv[i:])):
                iv[i+j] = code[i]
            cnt += 1
    print('#{} {}'.format(_+1, cnt))
