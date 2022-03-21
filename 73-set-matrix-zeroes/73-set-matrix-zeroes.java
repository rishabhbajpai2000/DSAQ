class Solution {
    public void setZeroes(int[][] matrix) {
        int[][] hash = new int[matrix.length][matrix[0].length];
        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix[i].length; j++) {
                if (matrix[i][j] == 0) {
                    hash[i][j] =1;
                }
            }
        }
        for (int i = 0; i < hash.length; i++) {
            for (int j = 0; j < hash[i].length; j++) {
                if (hash[i][j] == 1){
                    row_zero(matrix, i);
                    col_zero(matrix, j);
                }
                
            }
            
        }
    }

    public void row_zero(int[][] arr, int row) {
        for (int i = 0; i < arr[row].length; i++) {
            arr[row][i] = 0;
        }
    }

    public void col_zero(int[][] arr, int col) {
        for (int i = 0; i < arr.length; i++) {
            arr[i][col] = 0;
        }
    }
}
