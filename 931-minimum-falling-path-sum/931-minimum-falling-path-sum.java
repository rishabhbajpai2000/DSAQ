class Solution {
    public int minFallingPathSum(int[][] matrix) {
        // we are calculating the dp array
        int n = matrix.length;
        int[] dp = new int[n];

        for(int col = 0; col < n;col ++ )
            dp[col] = matrix[0][col];
        
        // any element in the dp array will be sum of its matrix counter part as well as
        // minimum of upper left upper right and upper directly 
        for(int row = 1;row<n;row++){
            int[] temp = new int[n];
            
            for(int col = 0;col<n;col++){
                int ul = 214748364;                
                if (col>0) ul = dp[col-1];
                
                 int ur = 214748364;
                if (col<n-1) ur = dp[col+1];
                
                int u = dp[col];
                
                temp[col] = matrix[row][col] + Math.min(ul, Math.min(u, ur));
            }
            
            for (int col = 0; col<n;col++) dp[col] = temp[col];
        }
        
        // The answer will be minimum of last row of dp array 
        int m = dp[0];
        for (int elem: dp) m = Math.min(m, elem);
        return m;
    }
    

}