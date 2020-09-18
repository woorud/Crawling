n = int(input())
n_list = [0] * 100000

for i in list(map(int, input().split())):
    n_list[i] = 1

m = int(input())
m_list = list(map(int, input().split()))
for i in m_list:
    if n_list[i] == 1:
        print('yes', end = ' ')
    else:
        print('no', end = ' ')