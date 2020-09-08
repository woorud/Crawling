n, m, k = map(int, input().split())
num_list = list(map(int, input().split()))
num_list.sort()
m1 = num_list[-1]
m2 = num_list[-2]

res = 0
while True:
    for i in range(k):
        if m == 0:
            break
        res += m1
        m -= 1
    if m == 0:
        break
    res += m2
    m -= 1
print(res)

M1 = num_list[n-1]
M2 = num_list[n-2]

cnt = m // (k+1) * k
cnt += m % (k+1)

res = 0
res += cnt * M1
res += (m-cnt) * M2

print(res)