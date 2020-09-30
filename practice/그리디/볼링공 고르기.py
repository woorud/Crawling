n, m = map(int, input().split())
weight = list(map(int, input().split()))
'''
res = []
for i in range(len(weight)):
    for j in range(i+1, len(weight)):
        if weight[i] != weight[j]:
            res.append((weight[i], weight[j]))

print(len(res))
'''

array = [0] * 11
for i in weight:
    array[i] += 1

res = 0
for i in range(1, len(weight)):
    n -= array[i]
    res += array[i] * n
print(res)