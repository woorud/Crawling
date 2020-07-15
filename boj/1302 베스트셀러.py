n = int(input())
books = {}

for i in range(n):
    book = input()
    if book not in books:
        books[book] = 1
    else:
        books[book] += 1

target = max(books.values())
res = []

for b, v in books.items():
    if target == v:
        res.append(b)
print(sorted(res)[0])