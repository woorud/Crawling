def solution(arr):
    answer = 0

    for i in arr:
        answer += i
        na = answer / len(arr)
    return na

