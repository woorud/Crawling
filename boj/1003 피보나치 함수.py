def count_fib(n):
    z = [1, 0]
    o = [0, 1]
    for i in range(2, n+1):
        z.append(z[i-1] + z[i-2])
        o.append(o[i-1] + o[i-2])
    return z, o

n = int(input())
z, o = count_fib(40)

for i in range(n):
    m = int(input())
    print('%d %d' %(z[m], o[m]))