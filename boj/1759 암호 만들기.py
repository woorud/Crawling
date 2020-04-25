from itertools import combinations
l, c = map(int, input().split())
dic_list = list(input().split())
dic = sorted(dic_list)
vowel = ['a', 'e', 'i', 'o', 'u']
vw = [i for i in dic if i in vowel]
comb = combinations(dic, l)

for i in comb:
    cnt = 0
    for j in i:
        if j in vw:
            cnt += 1

    if cnt >= 1 and cnt <= l-2:
        print(''.join(i))
