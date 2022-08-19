class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        m = nums[0]
        current_sum = 0 
        for i in nums:
            if current_sum < 0:
                current_sum = 0
            current_sum += i
            
            m = max(m, current_sum)
        return m
            
            