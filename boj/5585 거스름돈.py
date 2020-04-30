coin = [500, 100, 50, 10, 5, 1]
v = int(input())
change = 1000-v
cnt = 0
while change != 0:
    for i in coin:
        if i > change:
            pass
        else:
            tmp = change//i
            cnt += tmp
            change = change - i*tmp
print(cnt)