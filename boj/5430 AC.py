from collections import deque
t = int(input())
for i in range(t):
    function = list(input())
    n = int(input())
    arr = input()
    if n == 0:
        arr = []
    else:
        arr = deque(''.join(arr[1:-1]).split(','))
    cnt = 0
    tf = True

    for f in function:
        if f == 'R':
            cnt += 1
        elif f == 'D':
            if not arr:
                tf = False
                break
            if cnt % 2 == 0:
                arr.popleft()
            else:
                arr.pop()

    if not tf:
        print('error')
    else:
        if cnt % 2 == 0:
            print('[', end = '')
            print(','.join(arr), end = '')
            print(']')
        else:
            arr.reverse()
            print('[', end = '')
            print(','.join(arr), end = '')
            print(']')