'''
n = input()
l = [int(i) for i in n]
if l[:len(l)//2] == l[len(l)//2:]:
    print('LUCKY')
else:
    print('READY')
'''

n = input()
length = len(n)
s = 0

for i in range(length//2):
    s += int(n[i])

for i in range(length//2, length):
    s -= int(n[i])

if s == 0:
    print('LUCKY')
else:
    print('READY')