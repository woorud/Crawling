def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key = lambda x : x * 3, reverse = True) # 1000이하의 자연수이기 때문에 *3 을 통해 정렬
    return str(int(''.join(numbers)))

print(solution([6, 10, 2]))
print(solution([0, 0, 0]))
