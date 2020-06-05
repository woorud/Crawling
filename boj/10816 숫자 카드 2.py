def binary_Search(l, x):
    start = 0
    end = len(l) - 1
    while start <= end:
        mid = (start + end) // 2
        if l[mid] == x:
            return 1
        elif l[mid] > x:
            end = mid - 1
        else:
            start = mid + 1
    return 0

from collections import Counter
n = int(input())
card1 = list(map(int, input().split()))
card1.sort()
m = int(input())
card2 = list(map(int, input().split()))

c = Counter(card1)
res = [0 for i in range(m)]

for i in range(m):

    if binary_Search(card1, card2[i]):
        res[i] = c[card2[i]]

for i in res:
    print(i, end = ' ')