n = int(input())
age = []
for i in range(n):
    a, n = list(map(str, input().split()))
    age.append((int(a),n))
age.sort(key = lambda x : (x[0]))
for i in age:
    print(i[0], i[1])