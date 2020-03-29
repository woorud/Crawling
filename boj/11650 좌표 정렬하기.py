n = int(input())
l = []
for i in range(n):
    x, y = list(map(int, input().split()))
    l.append([x, y])

l.sort(key = lambda x : (x[0], x[1]))
for i in l:
    print(i[0], i[1])