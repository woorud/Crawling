def ascending(array):
    now = array[0]
    res = 1
    for i in range(1, len(array)):
        if now<array[i]:
            res += 1
            now = array[i]
    return res

n = int(input())
array = []


for i in range(n):
    array.append(int(input()))

print(ascending(array))
array.reverse()
print(ascending(array))