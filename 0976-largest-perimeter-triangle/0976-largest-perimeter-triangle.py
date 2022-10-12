class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        print(nums)
        for i in range(len(nums)-1, 1, -1):
            if nums[i] < nums[i-1] + nums[i-2]:
                return nums[i] + nums[i-1] + nums[i-2]
        return 0