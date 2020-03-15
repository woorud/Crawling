def solution(n):
    fib = [1, 1]
    for i in range(2, n):
        x = fib[i-2] + fib[i-1]
        fib.append(x)


    return fib[n-1] % 1234567

print(solution(3))
print(solution(5))