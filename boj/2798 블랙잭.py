from itertools import combinations as comb

a, b = map(int, input().split())
card_list = list(map(int, input().split()))

tl = []
for cards in comb(card_list, 3):
    tmp = sum(cards)
    if tmp <= b:
        tl.append(tmp)

print(max(tl))