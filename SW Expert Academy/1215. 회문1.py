def palindrome(s):
    if len(s) <= 1:
        return True
    else:
        for i in range(len(s)//2):
            if s[i] == s[len(s)-i-1]:
                continue
            else:
                return False
        return True

for i in range(10):
    length = int(input())
    matrix1 = []
    for j in range(8):
        matrix1.append(list(input()))
    matrix2 = []
    for a in range(8):
        tmp = []
        for b in range(8):
            tmp.append(matrix1[b][a])
        matrix2.append(tmp)

    cnt = 0
    for k in range(8):
       for l in range(8-length+1):
            if palindrome(matrix1[k][l:l+length]):
                cnt += 1
            if palindrome(matrix2[k][l:l+length]):
                cnt += 1
    print('#{} {}'.format(i+1, cnt))