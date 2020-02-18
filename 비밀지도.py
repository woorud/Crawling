def solution(n, arr1, arr2):
    answer = []

    for a, b in zip(arr1, arr2):
        x = str(bin(a | b))[2:]
        x = '0' * (n-len(x)) + x
        x = x.replace('1', '#')
        x = x.replace('0', ' ')
        answer.append(x)
    return answer







print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))