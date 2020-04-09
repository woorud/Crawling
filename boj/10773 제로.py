k = int(input())
stack = []
for i in range(k):
    x = int(input())
    if x != 0:
        stack.append(x)
    else:
        stack.pop()
print(sum(stack))