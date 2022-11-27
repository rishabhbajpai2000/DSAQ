class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [-1] * (n+1)
        
        def helper(index):
            if index == n:
                return 1
            if index > n:
                return 0
            if dp[index] != -1: return dp[index]
            
            dp[index] = helper(index + 1) + helper(index + 2)
            return dp[index]
    
        return helper(0)