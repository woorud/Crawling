n = int(input())
res = 0

for i in range(1, n+1):
    num_list = list(map(int, str(i)))
    res = i + sum(num_list)

    if n == res:
        print(i)
        break

    if n == i:
        print(0)