def solution(nums):
    can = []
    take = int(len(nums) / 2)
    nums.sort()
    can.append(nums[0])
    for i in range(1, len(nums)):
        if nums[i] > nums[i-1]:
            can.append(nums[i])
    if take < len(can):
        return take

    return len(can)


print(solution([3, 1, 2, 3]))
print(solution([3, 3, 3, 2, 2, 4]))