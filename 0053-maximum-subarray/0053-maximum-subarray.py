class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = nums[0]
        prefix = 0
        for i in nums:
            if prefix<0:
                prefix = 0
            prefix+= i
            ans = max(prefix, ans) 
        return ans