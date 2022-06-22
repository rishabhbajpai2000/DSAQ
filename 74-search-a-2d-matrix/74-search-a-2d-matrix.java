class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        
        int row = matrix.length-1; 
        
        for (int i = 0; i < matrix.length-1; i++){
            int first = matrix[i][0];
            int second = matrix[i+1][0];
            
            if (first == target || second == target) return true;
            
            if (first < target && second > target) row = i;
            
        }
        
        for (int i = 0 ; i<matrix[row].length; i++){
            if (matrix[row][i] == target)
                return true; 
        }
        
        return false;
    }
}