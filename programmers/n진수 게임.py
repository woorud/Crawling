def conv(number, base):
    t = '0123456789ABCDEF'
    i, j = divmod(number, base)
    if i == 0:
        return t[j]
    else:
        return conv(i, base) + t[j]

def solution(n, t, m, p):
    conv_list = []
    number = 0
    while len(conv_list) <= t*m:
        conv_list += list(conv(number, n))
        number += 1
    res = ''
    for i in range(t):
        res += conv_list[i*m+(p-1)]
    return res

print(solution(2, 4, 2, 1))
print(solution(16, 16, 2, 1))
print(solution(16, 16, 2, 2))