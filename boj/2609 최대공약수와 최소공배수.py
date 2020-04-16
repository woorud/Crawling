a, b = map(int, input().split())

n = []
for i in range(1, min(a, b)+1):
    if a % i == 0 and b % i == 0:
        n.append(i)

print(n[-1])
print((n[-1]) * (a//n[-1]) * (b//n[-1]))