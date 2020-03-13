score = []
for i in range(5):
    s = int(input())
    score.append(s)

for i in range(len(score)):
    if score[i] < 40:
        score[i] = 40
    else:
        score[i] = score[i]
print(sum(score) // len(score))
