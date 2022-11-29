class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        dp = [[-1] * len(text2) for _ in range(len(text1))]
        def helper(index1, index2):
            if index1 < 0 or index2 < 0:
                return 0
            if dp[index1][index2] != -1: return dp[index1][index2]
            
            dp[index1][index2] = 0
            if text1[index1] == text2[index2]: 
                dp[index1][index2] = 1 + helper(index1-1, index2-1)
            else:
                dp[index1][index2] = max(helper(index1-1, index2), helper(index1, index2-1))   
            return dp[index1][index2]
        
        
        index1, index2 = len(text1)-1, len(text2)-1
        return helper(index1, index2)