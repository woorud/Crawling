import sys
n = int(sys.stdin.readline())
if n == 0:
    print(0)

res = []
while n:
    if n % 2 == 1:
        res.append(1)
        n = n//-2 + 1
    else:
        res.append(0)
        n = n//-2


for i in reversed(res):
    print(i, end = '')