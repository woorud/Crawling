n, m = list(map(int, input().split()))
chess = []
nmin = 64
for i in range(n):
    chess.append(input())

for i in range(n-7):
    for j in range(m-7):
        c1 = 0
        c2 = 0
        for k in range(i, i+8):
            for s in range(j, j+8):
                if k%2 == 0 and s%2 == 0:
                    if chess[k][s] == 'B':
                        c1 += 1
                elif k%2 == 1 and s%2 == 1:
                    if chess[k][s] == 'B':
                        c1 += 1
                elif k%2 == 0 and s%2 == 1:
                    if chess[k][s] == 'W':
                        c1 += 1
                elif k%2 == 1 and s%2 == 0:
                    if chess[k][s] == 'W':
                        c1 += 1
        for k in range(i, i+8):
            for s in range(j, j+8):
                if k%2 == 0 and s%2 == 0:
                    if chess[k][s] == 'B':
                        c2 += 1
                elif k%2 == 1 and s%2 == 1:
                    if chess[k][s] == 'B':
                        c2 += 1
                elif k%2 == 0 and s%2 == 1:
                    if chess[k][s] == 'W':
                        c2 += 1
                elif k%2 == 1 and s%2 == 0:
                    if chess[k][s] == 'W':
                        c2 += 1

        min = min(nmin, c1, c2)
print(min)