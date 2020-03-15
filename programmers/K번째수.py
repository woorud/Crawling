def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        a = commands[i][0]
        b = commands[i][1]
        c = commands[i][2]
        l = array[a-1 : b]
        l.sort()
        answer.append(l[c-1])
    return answer



print(solution([1, 5, 2, 6, 3, 7, 4] , [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))