class Solution:

    def minDistance(self, word1: str, word2: str) -> int:
        l1 = len(word1)-1
        l2 = len(word2)-1
        
        dp = [[-1] * (l2+1) for _ in range(l1+1)]
        
        def helper(l1,l2):
            if l1<0: return l2 +1
            if l2 < 0: return l1 + 1
            if dp[l1][l2] != -1: return dp[l1][l2]
            if word1[l1] == word2[l2]:
                dp[l1][l2]=helper(l1-1, l2-1)
                return dp[l1][l2]
            dp[l1][l2]= 1 + min(helper(l1-1, l2), helper(l1, l2-1), helper(l1-1,l2-1))
            return dp[l1][l2]
        

        return helper(l1, l2)