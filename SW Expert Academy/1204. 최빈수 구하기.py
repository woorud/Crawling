t = int(input())

for _ in range(t):
    c = int(input())
    num_list = list(map(int, input().split()))

    dic = {}
    for i in num_list:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1

    dic = sorted(dic.items(), key = lambda x : x[1], reverse = True)

    print('#{} {}'.format(c, dic[0][0]))