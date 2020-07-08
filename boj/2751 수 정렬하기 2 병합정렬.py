def merge_sort(num_list):
    if len(num_list) <= 1:
        return num_list
    mid = len(num_list)//2
    left = merge_sort(num_list[:mid])
    right = merge_sort(num_list[mid:])
    i, j , k = 0, 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            num_list[k] = left[i]
            i += 1
        else:
            num_list[k] = right[j]
            j += 1
        k += 1
    if i == len(left):
        while j < len(right):
            num_list[k] = right[j]
            j += 1
            k += 1
    elif j == len(right):
        while i < len(left):
            num_list[k] = left[i]
            i += 1
            k += 1
    return num_list

n = int(input())
num_list = [int(input()) for i in range(n)]
num_list = merge_sort(num_list)
for i in num_list:
    print(i)