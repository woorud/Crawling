def _2447():
    def star(s):
        matrix = []
        for i in range(3*len(s)):
            if i//len(s) == 1:
                matrix.append(s[i%len(s)] + ' '*len(s) + s[i%len(s)])
            else:
                matrix.append(s[i%len(s)]*3)
        return matrix

    n = int(input())
    s = ['***', '* *', '***']

    k = 0
    while n != 3:
        n //= 3
        k += 1

    for i in range(k):
        s = star(s)
    for i in s:
        print(i)

_2447()
