n = int(input())
rope = [int(input()) for i in range(n)]
rope.sort(reverse=True)
ans = 0
for i in range(n):
    if ans < rope[i]*(i+1):
        ans = rope[i]*(i+1)
print(ans)