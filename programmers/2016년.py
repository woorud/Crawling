import datetime
def solution(a, b):
    date = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
    dt = datetime.date(2016, a, b).weekday()


    return date[dt]

print(solution(5, 24))