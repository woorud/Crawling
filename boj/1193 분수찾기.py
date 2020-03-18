n = int(input())

line = 1
while n > line:
    n -= line
    line += 1

if line % 2 == 0:
    a = n
    b = line-n+1
else:
    a = line-n+1
    b = n

print(a, '/', b, sep = '') #sep은 문자 사이에 띄어쓰기 사이에 다른 문자를 넣어준다.