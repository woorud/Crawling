c = int(input())
for _ in range(c):
    n, m = map(int, input().split())
    print_list = list(map(int, input().split()))
    prior = []
    for i in print_list:
        prior.append(i)

    res = [0] * n
    q = [i for i in range(n)]
    seq = 1
    while q:
        if print_list[q[0]] == max(prior):
            prior.remove(max(prior))
            res[q.pop(0)] = seq
            seq += 1
        else:
            q.append(q.pop(0))
    print(res[m])