n = int(input())
time = []
for i in range(n):
    time.append(list(map(int, input().split())))

time = sorted(time, key = lambda x : (x[1], x[0]))

cnt = 0
end = 0
for i in range(len(time)):
    if end <= time[i][0]:
        end = time[i][1]
        cnt += 1
print(cnt)