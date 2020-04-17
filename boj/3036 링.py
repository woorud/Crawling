from math import gcd
n = int(input())
r = list(map(int, input().split()))
for i in range(1, len(r)):
    x = gcd(r[0], r[i])
    print(str(r[0]//x) + '/' + str(r[i]//x))

