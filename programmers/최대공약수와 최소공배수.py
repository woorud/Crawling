from math import gcd
#Euclidean algofithm 사용하여 최대공약수와 최소공배수를 구할 수 있다.

def solution(n, m):
    answer = []
    a = gcd(n, m) #최대공약수
    b = (n * m) // a #최소공배수
    answer = [a, b]
    return answer


print(solution(3, 12))
print(solution(2, 5))