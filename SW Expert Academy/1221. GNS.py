num = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
num_list = {}
for a, b in enumerate(num):
    num_list[b] = a

t = int(input())
for i in range(t):
    a, b = input().split()
    nl = list(map(str, input().split()))
    res = ''
    tmp = sorted(nl, key = lambda x : num_list[x])
    for j in tmp:
        res += j + ' '
    print('{}\n{}'.format(a, res))