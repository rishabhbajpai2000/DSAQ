class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        l1 = len(word1)-1
        l2 = len(word2)-1
        
        dp = []
        # creating a dp array
        for i in range(l1+1):
            local = []
            for j in range(l2+1):
                local.append(-1)
            dp.append(local)
            
        def helper(i, j):
            if i<0: return j+1
            if j<0: return i+1
            if dp[i][j] != -1: return dp[i][j]
            
            if word1[i] == word2[j]: 
                dp[i][j] = helper(i-1,j-1)
                return dp[i][j] 
            
            dp[i][j] =  1 + + min(helper(i-1, j), helper(i,j-1), helper(i-1, j-1))
            return dp[i][j]
        

        return helper(l1, l2)