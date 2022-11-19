class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m = len(s)
        n = len(p)
        dp = [[-1] * m for _ in range(n)]
        
        def helper(i, j):
            # base cases 
            if i<0 and j<0:return True
            if i<0 and j>=0: return False
            if j<0 and i>= 0:
                for ii in range(i+1):
                    if p[ii] != "*": return False
                return True
            
            # dp case 
            if dp[i][j]!= -1:
                return dp[i][j]
            
            
            # match cases 
            if p[i]==s[j] or p[i]=="?":
                dp[i][j]= helper(i-1,j-1)
                return dp[i][j]
                
            if p[i] == "*":
                dp[i][j]= helper(i-1, j) or helper(i, j-1)
                return dp[i][j]
            dp[i][j] =  False
            return dp[i][j]
            
        return helper(n-1, m-1)