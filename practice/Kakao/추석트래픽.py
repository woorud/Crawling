def solution(lines):
    logs = []
    for line in lines:
        date, time, processing = line.split()
        h, m, s = time.split(':')
        end = (int(h)*3600 + int(m)*60 + float(s))*1000
        start = end - (float(processing[:-1])) * 1000 + 1
        logs.append([start, end])

    length = len(logs)
    max_value = 1
    for i in range(length-1):
        cnt = 1
        for j in range(i+1, length):
            if logs[j][1] - logs[i][1] >= 4000:
                break
            if logs[j][0] - logs[i][1] < 1000:
                cnt += 1
        max_value = max(max_value, cnt)
    return max_value


print(solution([
'2016-09-15 01:00:04.001 2.0s',
'2016-09-15 01:00:07.000 2s'
]))

print(solution([
'2016-09-15 01:00:04.002 2.0s',
'2016-09-15 01:00:07.000 2s'
]))

print(solution( [
'2016-09-15 20:59:57.421 0.351s',
'2016-09-15 20:59:58.233 1.181s',
'2016-09-15 20:59:58.299 0.8s',
'2016-09-15 20:59:58.688 1.041s',
'2016-09-15 20:59:59.591 1.412s',
'2016-09-15 21:00:00.464 1.466s',
'2016-09-15 21:00:00.741 1.581s',
'2016-09-15 21:00:00.748 2.31s',
'2016-09-15 21:00:00.966 0.381s',
'2016-09-15 21:00:02.066 2.62s'
]))
