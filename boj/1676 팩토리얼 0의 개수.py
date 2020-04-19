n = int(input())
cnt = 0
fac = 1

for i in range(1, n+1):
    fac = fac * i
for i in str(fac)[::-1]:
    if i == '0':
        cnt += 1
    else:
        break
print(cnt)