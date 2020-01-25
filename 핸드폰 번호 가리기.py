def solution(phone_number):
    l = list(phone_number)
    for i in range(0,len(l)-4):
        l[i] = "*"
    return "".join(l)

print(solution('01033334444'))