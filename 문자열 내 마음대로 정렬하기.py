def solution(strings, n):
    strings.sort()
    return sorted(strings, key = lambda strings : strings[n])





print(solution(['sun', 'bed', 'car'], 1))
print(solution(['abce', 'abcd', 'cdx'], 2))