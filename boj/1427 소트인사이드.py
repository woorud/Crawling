n = input()
num_list = []
for i in n:
    num_list.append(i)
num_list.sort(reverse = True)
res = ''
for i in num_list:
    res += i
print(int(res))