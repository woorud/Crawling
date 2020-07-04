n, m = map(int, input().split())
card = list(map(int, input().split()))
res = []
for i in range(0, len(card)):
    for j in range(i+1, len(card)):
        for k in range(j+1, len(card)):
            s = card[i] + card[j] + card[k]
            if s <= m:
                res.append(s)
print(max(res))