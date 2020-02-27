def solution(brown, red):
    for a in range(1, int(red**0.5)+1): # 두 자연수의 곱의 쌍에서 중복된 곱의 쌍을 없애기 위해서는 제곱근의 내림값보다 작거나 같다.
        if red % a == 0:
            b = red // a
            if 2*a + 2*b + 4 == brown:
                return [b+2, a+2]

print(solution(10, 2))
print(solution(8, 1))
print(solution(24, 24))