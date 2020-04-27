n = int(input())
t = list(map(int, input().split()))
people = []
for i in range(len(t)):
    time = [i+1, t[i]]
    people.append(time)
people = sorted(people, key = lambda x : (x[1], x[0]))

time = 0
for i in range(len(people)):
    time += people[i][1] * (n-i)

print(time)