class Solution {
    public boolean checkXMatrix(int[][] grid) {
       int len = grid.length;
        for (int i = 0; i<len; i++){
            for (int j = 0; j< len;j++){
                // diagonal condition
                if (i == j || i+j == len-1){
                    if (grid[i][j] == 0) return false;}
                // other than diagonal elements
                else if(grid[i][j] != 0) return false;
            }
        }
        return true;
    }
}