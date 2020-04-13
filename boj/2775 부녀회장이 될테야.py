t = int(input())
for i in range(t):
    k = int(input())
    n = int(input())

    people = []
    for j in range(1, n+1):
        people.append(j)

    for l in range(k):
        for m in range(n-1):
            people[m+1] += people[m]
    print(people[-1])
