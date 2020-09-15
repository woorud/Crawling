N = int(input())
p = [input() for i in range(N)]
s = [input() for i in range(N-1)]

d = {}

for i in p:
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1

for j in s:
    if j in d:
        d[j] -= 1

for k, v in d.items():
    if v == 1:
        print(k)