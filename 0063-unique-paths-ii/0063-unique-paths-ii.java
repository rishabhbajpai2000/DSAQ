class Solution {
    public int uniquePathsWithObstacles(int[][] obstacleGrid) {
        int m = obstacleGrid.length;
        int n = obstacleGrid[0].length;
        
        int[][] dp = new int[m+1][n+1];
        for(int[] arr:dp) Arrays.fill(arr, -1);
        return f(dp, m-1, n-1, obstacleGrid);
    }
    
    int f(int[][]dp, int m, int n, int[][] obstacleGrid){
        if (m<0 || n<0) return 0;
        if (obstacleGrid[m][n] == 1) return 0;
        if (m == 0 && n==0) return 1;
        
        if (dp[m][n] != -1) return dp[m][n];
        
        return dp[m][n] = f(dp, m-1, n, obstacleGrid) + f(dp, m, n-1,obstacleGrid);
    }
}