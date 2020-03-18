import math
A, B, V = list(map(int, input().split()))
distance = A - B
print(math.ceil((V-A)/(distance))+1)
