class Solution {
    public void rotate(int[][] matrix) {
        
        // first we need to take transpose inplace
        for (int i = 0; i < matrix.length; i++) {
           for (int j = 0; j <= i ; j++) {
            int temp = matrix[i][j];
            matrix[i][j] = matrix[j][i];
            matrix[j][i] = temp;
            
           } 
        }
        
        // now we need to interchange columns
        // first from last, second from second last, third from third last and so on 
        int cols = matrix.length;
        for (int i = 0; i<cols/2; i++){
            interchng_col(matrix, i, cols-i-1);
        }
        
    }
    
   void interchng_col(int[][] matrix, int col1, int col2){
        for(int i = 0; i<matrix.length; i++){
            // matrix[i][col1], matrix[i][col2] need to be interchanged;
            int temp = matrix[i][col1];
            matrix[i][col1] = matrix[i][col2];
            matrix[i][col2] = temp;
        }
        
    }
}