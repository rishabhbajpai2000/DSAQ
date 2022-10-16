class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums = set(nums)
        m = -1
        for i in nums:
            if -1*i in nums: m = max(i, m)
        return m