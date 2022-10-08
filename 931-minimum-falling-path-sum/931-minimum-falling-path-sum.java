class Solution {
    public int minFallingPathSum(int[][] matrix) {
        int n = matrix.length;
        int[][] dp = new int[n][n];
        int row = 0;
        for(int col = 0; col < n;col ++ )
            dp[row][col] = matrix[row][col];
        
        for(row = 1;row<n;row++){
            for(int col = 0;col<n;col++){
                int ul = 214748364;
                int ur = 214748364;
                
                if (col>0) ul = dp[row-1][col-1];
                int u = dp[row-1][col];
                if (col<n-1) ur = dp[row-1][col+1];
                
                dp[row][col] = matrix[row][col] + Math.min(ul, Math.min(u, ur));
            }
        }
        
        row = n-1;
        int m = dp[row][0];
        for (int col = 0; col<n;col++)
            m = Math.min(m, dp[row][col]);
        

        
        return m;
    }
    

}