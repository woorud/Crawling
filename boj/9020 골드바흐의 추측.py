def solution(n):
    pl = [False, False] + [True] * (n-1)

    primes = []
    for i in range(2, n+1):
        if pl[i] == True:
            for j in range(2*i, n+1, i):
                pl[j] = False
            primes.append(i)
    return primes

num_list = []
for i in range(int(input())):
    num_list.append(int(input()))

for n in num_list:
    l = solution(n)
    a = n // 2

    for i in range(a, 1, -1):
        if i in l and n-i in l:
            print(i, n-i)
            break