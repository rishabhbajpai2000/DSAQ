class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # dp = [[-1] * len(t) for _ in range(len(s))]
        
        @lru_cache(maxsize = None)
        def helper(i, j):
            if j<0: return 1
            if i<0: return 0
            
            if s[i] == t[j]:
                return helper(i-1,j-1) + helper(i-1,j)
            return helper(i-1,j)

        
        return helper(len(s)-1,len(t)-1)