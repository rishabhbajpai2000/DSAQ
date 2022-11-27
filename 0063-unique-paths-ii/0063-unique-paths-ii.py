class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        dp = [[-1] * len(grid[0]) for _ in range(len(grid))]
            
        def helper(x, y):
            
            if x == len(grid)-1 and y == len(grid[0])-1 and grid[x][y] == 0: return 1
            if x > len(grid)-1 or y > len(grid[0])-1: return 0
            if grid[x][y] == 1: return 0
            if dp[x][y] != -1: return dp[x][y]

            dp[x][y] = helper(x+1, y) + helper(x, y+1)
            return dp[x][y]
        return helper(0,0)