from collections import deque

def solution(s):
    s = deque(list(s))
    al = []
    al.append(s.popleft())
    while s:
        if len(al) == 0 :
            al.append(s.popleft())
        elif al[-1] == s[0]:
            al.pop()
            s.popleft()
        else:
            al.append(s.popleft())

    if len(al) != 0:
        return 0
    else:
        return 1


print(solution('baabaa'))