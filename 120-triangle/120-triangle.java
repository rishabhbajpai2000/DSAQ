class Solution {
    public int minimumTotal(List<List<Integer>> triangle) {
        int size = triangle.size();
        int[][] dp= new int[size][size];
        for(int[] arr: dp) Arrays.fill(arr, -1);
        int row = 0;
        int col = 0;
        return helper(triangle, row, col, dp);
    }
    
    int helper(List<List<Integer>> triangle, int row, int col,int[][] dp){
        if (row == triangle.size() - 1) return triangle.get(row).get(col);
        if (dp[row][col] != -1) return dp[row][col];
        
        int down = triangle.get(row).get(col) + helper(triangle, row + 1, col, dp);
        int right = triangle.get(row).get(col) + helper(triangle, row + 1, col + 1, dp);
        
        
        return dp[row][col] = Math.min(down, right);
    
    }
}