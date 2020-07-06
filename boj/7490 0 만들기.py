import copy
def recursive(array, n):
    if len(array) == n:
        operators_list.append(copy.deepcopy(array)) # copy: list 내용을 항상 복사해서 넣음
        return
    array.append(' ')
    recursive(array, n)
    array.pop()

    array.append('+')
    recursive(array, n)
    array.pop()

    array.append('-')
    recursive(array, n)
    array.pop()

t = int(input())
for _ in range(t):
    operators_list = []
    n = int(input())
    recursive([], n-1)

    integers = [i for i in range(1, n+1)]

    for o in operators_list:
        string = ''
        for i in range(n-1):
            string += str(integers[i]) + o[i]
        string += str(integers[-1])
        if eval(string.replace(' ', '')) == 0:
            print(string)