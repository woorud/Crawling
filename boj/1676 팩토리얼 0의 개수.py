def fac(n):
    if n == 1:
        return 1
    else:
        return n*fac(n-1)

n = int(input())
num = list(str(fac(n)))
cnt = 0

for i in num[::-1]:
    if i == '0':
        cnt += 1
    else:
        print(cnt)
        break

