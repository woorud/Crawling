def solution(s):
    s = s.split(' ')
    answer = ""

    for i in s:
        i = i.capitalize()
        answer += i + ' '
    return answer[: -1]



print(solution('3people unFollowed me'))
print(solution('for the last week'))