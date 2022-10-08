class Solution {
    public int minFallingPathSum(int[][] matrix) {
        
        int[][] dp = new int[matrix.length][matrix.length];
        for(int[] arr: dp)Arrays.fill(arr, -1);
        
        int mini = 214748364;
        int row = 0;
        
        for (int col = 0; col<matrix.length; col++)
            mini = Math.min(mini, helper(dp, matrix, row, col));
        
        return mini;
    }
    
    int helper(int[][] dp, int[][] matrix, int row, int col){
        if (row == matrix.length - 1)
            return matrix[row][col];

        if (dp[row][col] != -1)
            return dp[row][col];

        int u_u = matrix[row][col] + helper(dp, matrix, row + 1, col);
        int u_l = 21474836;
        if (col>0) u_l = matrix[row][col] + helper(dp, matrix, row + 1, col - 1);
        int u_r = 21474836;
        if (col<matrix.length-1) u_r = matrix[row][col] + helper(dp, matrix, row + 1, col + 1);

        return dp[row][col] = Math.min(u_l, Math.min(u_u, u_r));
        
        
    }
}