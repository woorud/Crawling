def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        x = []
        for j in range(len(arr2[0])):
            tmp = 0
            for k in range(len(arr1[0])):
                tmp += arr1[i][k] * arr2[k][j]
            x.append(tmp)
        answer.append(x)

    return answer

print(solution([[1, 4], [3, 2], [4, 1]], [[3, 3], [3, 3]]))