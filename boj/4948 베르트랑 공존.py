def solution(n):
    pl = [False, False] + [True] * ((2*n)-1)
    for i in range(2, ((2*n)+1)):
        if pl[i] == True:
            for j in range(2*i, ((2*n)+1), i):
                pl[j] = False
    return pl

while True:
    n = int(input())
    if n == 0:
        break
    l = solution(n)
    cnt = 0
    for i in range(n+1, (2*n)+1):
        if l[i] == True:
            cnt +=1
    print(cnt)