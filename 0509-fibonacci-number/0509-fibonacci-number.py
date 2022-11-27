class Solution:
    def fib(self, n: int) -> int:
        
        def helper(n):
            if n<=1:return n
            if dp[n] != -1: return dp[n]
            dp[n] = helper(n-1) + helper(n-2)
            return dp[n]
        
        
        dp = [-1] * (n+1)
        return helper(n)
        