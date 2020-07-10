document = input()
word = input()

idx = 0
res = 0

while len(document) - idx >= len(word):
    if document[idx:idx+len(word)] == word:
        idx += len(word)
        res += 1
    else:
        idx += 1
print(res)
