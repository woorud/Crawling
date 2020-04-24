min, max = map(int, input().split())
num = [True] * (max-min+1)
cnt = 0
n = 1

while n*n <= max:
    n += 1
    square = n*n
    i = min // square

    while square * i <= max:
        idx = square * i - min

        if idx >= 0 and num[idx]:
            cnt += 1
            num[idx] = False

        i += 1
print(len(num)-cnt)