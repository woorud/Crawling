n = int(input())

stack = []
res = []
cnt = 1

for i in range(1, n+1):
    num = int(input())
    while cnt <= num:
        stack.append(cnt)
        cnt += 1
        res.append('+')
    if stack[-1] == num:
        stack.pop()
        res.append('-')
    else:
        print('NO')
        break
print('\n'.join(res))