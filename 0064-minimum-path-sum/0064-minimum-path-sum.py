class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        dp = [[-1]*cols for _ in range(rows)]
        
        def helper(row, col):
            if row == rows-1 and col == cols-1:
                return grid[row][col]
            if row > rows-1 or col > cols-1:
                return 1_000_000_0009
            
            if dp[row][col] != -1: 
                return dp[row][col]
            
            dp[row][col] = grid[row][col] + min(helper(row+1, col), helper(row, col+1))
            return dp[row][col]
            # return grid[row][col] + min(helper(row+1, col), helper(row, col+1))
        
        return helper(0,0)