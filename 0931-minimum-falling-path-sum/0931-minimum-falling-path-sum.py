class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        
        dp = [[-1] * cols for _ in range(rows)]
        
        def helper(row, col):
            if col > cols-1 or col < 0:
                return 1_000_000_009
            if row == rows-1:                    
                return matrix[row][col]
            
            if dp[row][col] != -1: return dp[row][col]

            dp[row][col] =  matrix[row][col] + min(helper(row+1,col-1), helper(row+1, col), helper(row+1, col+1))
            return dp[row][col]
        
        ans = helper(0,0)
        
        for col in range(1,cols):
            ans = min(ans, helper(0, col))
        
        return ans