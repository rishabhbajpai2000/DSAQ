class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(index, nums, dp):
            if index >= len(nums):
                return 0
            if dp[index] != -1: return dp[index]
            
            chosen = nums[index] + helper(index+2, nums, dp)
            not_chosen = helper(index+1, nums, dp)
            
            dp[index] = max(chosen, not_chosen)
            return dp[index]
        
        if len(nums) == 1: return nums[0]
        last = nums[-1]
        nums = nums[:-1]
        dp = [-1] * len(nums)
        ans1 = helper(0, nums, dp)
        
        
        nums.append(last)
        dp = [-1] * len(nums)
        nums = nums[1:]
        ans2 = helper(0, nums, dp)
        
        return max(ans1, ans2)
        
        