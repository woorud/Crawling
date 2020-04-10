n = int(input())
cnt = 1
stack = []
res = []
p = True
for i in range(n):
    num = int(input())
    while cnt <= num:
        stack.append(cnt)
        res.append('+')
        cnt += 1
    if stack[-1] == num:
        stack.pop()
        res.append('-')
    else:
        p = False

if p == False:
    print('NO')
else:
    for i in res:
        print(i)