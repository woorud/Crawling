def binary_search(l, x):
    start = 0
    end = len(l) - 1

    while start <= end:
        mid = (start + end) // 2
        if x == l[mid]:
            return 1
        elif x > l[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return 0

n = int(input())
a = list(map(int, input().split()))
a.sort()
m = int(input())
b = list(map(int, input().split()))

for i in b:
    print(binary_search(a, i))

