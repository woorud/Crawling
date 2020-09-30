s = input()
num = [int(i) for i in s]

res = num[0]
for i in range(1, len(num)):
    if num[i] <= 1 or res <= 1:
        res += num[i]
    else:
        res *= num[i]

print(res)