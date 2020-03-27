A, B = input().split()

min = len(A)
for i in range(len(B)-len(A)+1):
    cnt = 0
    for j in range(len(A)):
        if A[j] != B[i+j]:
            cnt += 1
    if cnt < min:
        min = cnt

print(min)

