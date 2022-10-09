class Solution {
    int mod = 1000_000_007;
    public int numberOfPaths(int[][] grid, int k) {
        int m = grid.length;
        int n = grid[0].length;
        int[][][] dp = new int[m][n][k];
        for(int[][] arr:dp){
            for(int[] a: arr) 
                Arrays.fill(a, -1);
        }
        
        
        
        return memo(grid, m-1, n-1, 0, k, dp);
    }
    
    int memo(int[][] grid, int m, int n, int sum, int k, int[][][] dp){
        
        if (m<0 || n< 0) return 0;
        
        if (m == 0 && n == 0){
            sum += grid[m][n];
            return sum%k==0?1:0;
        }
        
        if (dp[m][n][sum%k] != -1) return dp[m][n][sum%k];
        
        int left = memo(grid, m, n-1, (sum + grid[m][n])%k, k, dp);
        int right = memo(grid, m-1, n, (sum + grid[m][n])%k, k, dp);
        
        return dp[m][n][sum%k] = (left+right)%mod;
    }
}