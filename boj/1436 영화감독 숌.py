n = int(input())
cnt = 0
m = 666
while True:
    if '666' in str(m):
        cnt += 1
    if cnt == n:
        print(m)
        break
    m += 1

