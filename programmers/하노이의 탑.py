res = []
def hanoi(n, start, to, end):
    if n == 1:
        res.append([start, end])
    else:
        hanoi(n-1, start, end, to) # n-1 개의 원판을 첫번째에서 두번째로
        hanoi(1, start, to, end) # 1개의 원판을 첫번째에서 마지막으로
        hanoi(n-1, to, start, end) # n-1 개의 원판을 두번째에서 마지막으로
    return res

def solution(n):
    answer = hanoi(n, 1, 2, 3)
    return answer

print(solution(2))