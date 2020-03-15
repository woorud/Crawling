n = int(input())
num_list = list(map(int, input().split()))

cnt = 0
for i in num_list:
    dc = 0
    if i == 1:
        continue
    for j in range(1, 1000):
        if i % j == 0:
            dc += 1
    if dc == 2:
        cnt += 1
print(cnt)

