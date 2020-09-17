n = int(input())
students = []
for i in range(n):
    data = input().split()
    students.append((data[0], int(data[1])))

for i in sorted(students, key = lambda x : x[1]):
    print(i[0], end = ' ')

