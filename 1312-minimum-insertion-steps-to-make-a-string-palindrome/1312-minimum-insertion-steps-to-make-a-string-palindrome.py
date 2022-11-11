class Solution:
    def minInsertions(self, s: str) -> int:
        

        def longestCommonSubsequence( text1: str, text2: str) -> int:
            dp = []
            for i in range(len(text1)):
                local = []
                for j in range(len(text2)):
                    local.append(-1)
                dp.append(local)


            def helper(ind1, ind2):
                if ind1 < 0 or ind2 <0: return 0
                if dp[ind1][ind2] != -1: return dp[ind1][ind2]

                if text1[ind1] == text2[ind2]:
                    return 1 + helper(ind1-1, ind2-1)

                dp[ind1][ind2] = max(helper(ind1-1, ind2), helper(ind1, ind2-1))
                return dp[ind1][ind2]

            return helper(len(text1)-1, len(text2)-1)


        
        return len(s) - longestCommonSubsequence(s, s[::-1])
    