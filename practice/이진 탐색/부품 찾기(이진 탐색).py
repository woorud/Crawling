def binary_search(array, target, start, end):
    while start <= end:
        mid = (start+end)//2
        if array[mid] == target:
            return True
        elif array[mid] > target:
            end = mid-1
        else:
            start = mid +1
    return None

n = int(input())
n_list = list(map(int, input().split()))
m = int(input())
m_list = list(map(int, input().split()))
n_list.sort()

for i in range(len(m_list)):
    res = binary_search(n_list, m_list[i], 0, len(n_list)-1)
    if res:
        print('yes', end = ' ')
    else:
        print('no', end = ' ')


