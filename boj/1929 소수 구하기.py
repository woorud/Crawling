m, n = list(map(int, input().split(' ')))

pl = [False, False] + [True] * (n-1)

primes = []
for i in range(2, n+1):
    if pl[i] == True:
        for j in range(2*i, n+1, i):
            pl[j] = False

for k in range(m, n+1):
    if pl[k] == True:
        print(k)