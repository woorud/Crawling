n = int(input())
num_list = list(map(int, input().split()))
tmp = [0 for i in range(n)]
res = -1001

for i in range(n):
    tmp[i] = max(tmp[i-1] + num_list[i], num_list[i])
    res = max(res, tmp[i])
print(res)