### 최소공배수는 주어진 수의 곱을 주어진 수의 최대공약수로 나눈 것과 같다.###
from math import gcd
def lcm(x, y):
    return x*y // gcd(x, y)

def solution(arr):

    while len(arr) != 1:
        arr.append(lcm(arr.pop(), arr.pop()))
    return arr[0]



print(solution([2, 6, 8, 14]))
