num_list = list(map(int, input().split()))

ascending = True
descending = True

for i in range(1, len(num_list)):
    if num_list[i] > num_list[i-1]:
        descending = False
    elif num_list[i] < num_list[i-1]:
        ascending = False

if ascending:
    print('ascending')
elif descending:
    print('descending')
else:
    print('mixed')