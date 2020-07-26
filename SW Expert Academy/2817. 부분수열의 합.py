def solution(idx, sum):
    global cnt
    if idx >= n:
        return
    tmp = sum + num_list[idx]
    if tmp == k:
        cnt += 1
    solution(idx+1, sum)
    solution(idx+1, tmp)
    
t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    num_list = list(map(int, input().split()))
    cnt = 0
    solution(0, 0)
    print('#{} {}'.format(_+1, cnt))