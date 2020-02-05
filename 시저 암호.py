def solution(s, n):
    A = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    a = A.lower()
    answer = ''

    for i in s:
        if i.isupper():
            idx = (A.index(i) + n) % 26
            answer += A[idx]
        elif i.islower():
            idx = (a.index(i) + n) % 26
            answer += a[idx]
        else:
            answer += ' '
    return answer






print(solution('a B', 1))