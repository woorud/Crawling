def solution(n):
    tf = [False, False] + [True] * (n-1)

    primes = []
    for i in range(2, n+1):
        if tf[i] == True:
            primes.append(i)
            for j in range(2*i, n+1, i):
                tf[j] = False
    return len(primes)
print(solution(10))
print(solution(5))