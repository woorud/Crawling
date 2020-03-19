c = int(input())
for i in range(c):
    h, w, n = map(int, input().split())

    if n % h == 0:
        f = h * 100
        ho = n // h
    else:
        f = (n % h) * 100
        ho = 1 + n // h
    print(f + ho)
