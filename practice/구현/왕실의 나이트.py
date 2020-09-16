rc = input()
r = int(rc[1])
c = int(ord(rc[0])) - int(ord('a')) + 1
moves = [
    (-2,-1), (-1,-2), (-1, 2), (2, -1),
    (2, 1), (1, 2), (1, -2), (-2, 1)
]

res = 0
for i in moves:
    next_r = r + i[0]
    next_c = c + i[1]
    if next_r >= 1 and next_r <= 8 and next_c >= 1 and next_c <= 8:
        res += 1
print(res)