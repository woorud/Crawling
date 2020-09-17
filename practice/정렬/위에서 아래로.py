n = int(input())
numbers = [int(input()) for i in range(n)]
for i in sorted(numbers, reverse = True):
    print(i, end = ' ')