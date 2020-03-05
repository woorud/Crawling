def findPrime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def solution(nums):
    nl = []
    for i in range(len(nums)-2):
        for j in range(i+1, len(nums)-1):
            for l in range(j+1, len(nums)):
                nl.append(nums[i] + nums[j] + nums[l])

    cnt = 0
    for i in nl:
        if findPrime(i) == True:
            cnt += 1
    return cnt


print(solution([1, 2, 3, 4]))
print(solution([1, 2, 7, 6, 4]))