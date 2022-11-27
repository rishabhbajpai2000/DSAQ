class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        def helper(row, col):
            if row == m-1 and col == n-1: return 1
            if row > m-1 or col > n-1: return 0
            if dp[row][col] != -1: return dp[row][col]
            
            dp[row][col] = helper(row+1, col) + helper(row, col+1)
            return dp[row][col]
        
        dp = [[-1] * (n) for _ in range(m)]
        
        return helper(0,0)