t = int(input())

for i in range(t):
    n = int(input())

    if n == 0:
        print(0)
        continue

    wear = dict()
    for j in range(n):
        name, type = list(map(str, input().split()))

        if type in wear.keys():
            wear[type] += 1
        else:
            wear[type] = 1

        answer = 1
        for k in wear.keys():
            answer *= wear[k] + 1
    print(answer - 1)