mod = list(input().split('-'))
res = 0

for i in mod[0].split('+'):
    res += int(i)

for i in mod[1:]:
    for j in i.split('+'):
        res -= int(j)

print(res)