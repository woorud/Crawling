s = input()

a = []
n = 0

for i in s:
    if i.isalpha():
        a.append(i)
    else:
        n += int(i)
print(''.join(sorted(a)) + str(n))
