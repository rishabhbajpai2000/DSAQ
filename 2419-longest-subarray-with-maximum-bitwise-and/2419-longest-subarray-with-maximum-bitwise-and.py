class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        m = max(nums)
        count = 1
        local = 0
        for i in nums:
            if i == m:
                local += 1
                count = max(count, local)
            else:
                local = 0
            
        return count
        