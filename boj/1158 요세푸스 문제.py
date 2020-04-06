n, k = list(map(int, input().split()))

l = []
for i in range(1, n+1):
    l.append(i)

idx = k-1
res = []
while True:
    res.append(l.pop(idx))
    if not l:
        break
    idx = (idx+k-1) % len(l)

print('<' + ', '.join(map(str, res)) + '>')