def left(index, nums):
    for i in range(index, -1, -1):
        if nums[i] != nums[index]:
            return nums[i]
    return -1

def right(index, nums):
    for i in range(index, len(nums)):
        if nums[i] != nums[index]:
            return nums[i]
    return -1

class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        count = 0
        for i in range(1, len(nums)-1):
            left_n = left(i, nums)
            right_n = right(i, nums)
            if nums[i-1] == nums[i] or left_n == -1 or right_n == -1: count += 0
            elif left_n < nums[i] and right_n<nums[i]: 
                count += 1
                print(nums[i])
            elif left_n > nums[i] and right_n > nums[i]: 
                count += 1
                print(nums[i])
        return count