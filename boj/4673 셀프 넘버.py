num = set()
for i in range(1, 10001):
    num.add(i)

notself_num = set()
for i in range(1, 10001):
    for j in str(i):
        i = i + int(j)
    notself_num.add(i)

self_num = num - notself_num
for i in self_num:
    print(i)


