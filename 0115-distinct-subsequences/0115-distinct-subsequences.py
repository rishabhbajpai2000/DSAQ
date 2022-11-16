class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = []
        for i in range(len(s)):
            local = []
            for i in range(len(t)):
                local.append(-1)
            dp.append(local)
        
        def helper(i, j):
            if j<0: return 1
            if i<0: return 0
            
            
            if dp[i][j] != -1: return dp[i][j]
            
            if s[i] == t[j]:
                dp[i][j] = helper(i-1,j-1) + helper(i-1,j)
                return dp[i][j]
            
            dp[i][j] = helper(i-1,j)
            return dp[i][j]
        
        return helper(len(s)-1,len(t)-1)