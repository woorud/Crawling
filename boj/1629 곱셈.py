# a = nc + r
# a**2 = (nc)**2 + 2ncr + r**2
# a**2 % c = r**2 % c

def squared(a, b):
    if b == 0:
        return 1
    elif b == 1:
        return a
    elif b % 2 == 1:
        return squared(a, b-1) * a
    half = squared(a, b//2)
    half %= c
    return half ** 2 % c

a, b, c = map(int, input().split())
print(squared(a, b) % c)
