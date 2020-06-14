n = int(input())
num_list = list(map(int, input().split()))

dpi = [0 for i in range(n)]
dpd = [0 for i in range(n)]

for i in range(n):
    dpi[i] = 1
    for j in range(i):
        if num_list[j] < num_list[i]:
            dpi[i] = max(dpi[i], dpi[j]+1)

for i in range(n-1, -1, -1):
    dpd[i] = 1
    for j in range(n-1, i-1, -1):
        if num_list[j] < num_list[i]:
            dpd[i] = max(dpd[i], dpd[j]+1)

cnt = 0
for i in range(n):
    if cnt < dpi[i] + dpd[i]-1:
        cnt = dpi[i] + dpd[i]-1

print(dpi, dpd, cnt)