class Solution {
    public int maxSum(int[][] grid) {
        // if i, j is the first index then hour glass will be
        // i,j; i, j+1; i, j+2;
        //     i+1, j+1;
        // i+2, j; i+1, j+1; i+2, j+2
        
        int s = 0;
        for (int row = 0; row<grid.length-2; row++){
            for (int col =0; col<grid[row].length-2; col++){
                s = Math.max(s, score(grid, row, col));
            }
        }
        return s;
    }
    
    int score(int[][]grid, int row, int col){
        int score = grid[row][col] + grid[row][col+1] + grid[row][col+2];
        score += grid[row+1][col+1];
        score+= grid[row+2][col] + grid[row+2][col+1] + grid[row+2][col+2];
        return score;
    }
}