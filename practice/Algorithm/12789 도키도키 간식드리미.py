n = int(input())
order = list(map(int, input().split()))
st = []
q = []
num = 1

while order:
    tmp = order.pop(0)
    if num == tmp:
        st.append(tmp)
        num += 1
    else:
        q.append(tmp)
while q:
    tmp = q.pop()
    if st[-1] + 1 == tmp:
        st.append(tmp)
    else:
        print('Sad')
        break

if len(st) == n:
    print('Nice')