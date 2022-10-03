class Solution {
    public int minPathSum(int[][] grid) {
        int m = grid.length;
        int n = grid[0].length;
        int[][] dp = new int[m][n];
        return helper(m-1,n-1, dp, grid);
    }
    
    int helper(int m, int n, int[][] dp, int[][] grid){
        if (m<0||n<0) return 1000;
        if (m == 0 && n == 0) return grid[m][n];
        
        if (dp[m][n] != 0) return dp[m][n];
        
        int up =grid[m][n]+ helper(m-1, n, dp, grid);
        int left = grid[m][n]+helper(m, n-1, dp, grid);
        
        return dp[m][n] = Math.min(up, left);
    }
} 