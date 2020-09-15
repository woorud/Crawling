n, m = map(int, input().split())
monster = [input() for i in range(n)]
p = [input() for i in range(m)]

for i in p:
    try:
        i = int(i)
        print(monster[i-1])
    except:
        print(monster.index(i)+1)
