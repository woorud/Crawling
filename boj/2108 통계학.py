import sys
from collections import Counter
n = int(input())
l = []
for i in range(n):
    x = int(sys.stdin.readline())
    l.append(x)

def mode(l):
    d = Counter(l)
    modes = d.most_common()
    if len(l) > 1:
        if modes[0][1] == modes[1][1]:
            return modes[1][0]
        else:
            return modes[0][0]
    else:
        return modes[0][0]

print(round(sum(l)/len(l)))

l.sort()
print(l[len(l)//2])

print(mode(l))

print(l[-1]-l[0])


