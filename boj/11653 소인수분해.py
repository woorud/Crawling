n = int(input())
res = []
while n != 1:
    for i in range(2, n+1):
        if n % i == 0:
            res.append(i)
            n = n // i
            break
for i in res:
    print(i)