m = int(input())
n = int(input())

l = []
for i in range(m, n+1):
    dc = 0
    for j in range(1, n+1):
        if i % j == 0:
            dc += 1
            if dc > 2:
                break
    if dc == 2:
        l.append(i)
if len(l) == 0:
    print(-1)
else:
    print(sum(l))
    print(min(l))
