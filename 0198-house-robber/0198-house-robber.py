class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def helper(index):
            if index >= len(nums):
                return 0
            if dp[index] != -1: return dp[index]
            
            chosen = nums[index] + helper(index+2)
            not_chosen = helper(index+1)
            
            dp[index] = max(chosen, not_chosen)
            return dp[index]
        
        dp = [-1] * len(nums)
        return helper(0)