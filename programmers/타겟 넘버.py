import copy
def recursive(array, n):
    if len(array) == n:
        operators_list.append(copy.deepcopy(array)) # copy: list 내용을 항상 복사해서 넣음
        return

    array.append('+')
    recursive(array, n)
    array.pop()

    array.append('-')
    recursive(array, n)
    array.pop()


def solution(numbers, target):
    operators_list = []
    recursive([], len(numbers))

print(solution([1,1,1,1,1], 3))