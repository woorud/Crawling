n = int(input())
sec = 0
k = 1

while n != 0:
    if n-k > k:
        n -= k
        k += 1
    else:
        n -= k
        k = 1

    sec += 1

print(sec)
