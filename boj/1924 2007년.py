date = 0
month = [31,28,31,30,31,30,31,31,30,31,30,31]
day = ['SUN' ,'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
m, d = list(map(int, input().split()))

for i in range(m-1):
    date = date + month[i]
date = (date+d) % 7
print(day[date])
