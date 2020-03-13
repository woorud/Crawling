n = int(input())

if n == 1:
    print('*')
else:
    if n % 2 == 0:
        a = '* ' * (n//2)
        b = ' *' * (n//2)
    else:
        a = '* ' * (n//2) + '*'
        b = ' *' * (n//2)
    for i in range(n):
        print(a)
        print(b)
