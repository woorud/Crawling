import sys
n = int(input())
l = [0] * 10001

for i in range(n):
    f = int(sys.stdin.readline())
    l[f] = l[f] + 1

for i in range(10001):
    if l[i] != 0:
        for j in range(l[i]):
            print(i)