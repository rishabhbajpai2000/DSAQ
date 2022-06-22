class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        
        int row = matrix.length-1; 
        
        for (int i = 0; i < matrix.length-1; i++){
            int first = matrix[i][0];
            int second = matrix[i+1][0];
            
            if (first == target || second == target) return true;
            if (first < target && second > target) row = i;
            
        }
        
        if (binary_search(matrix, row, target)) return true;
        
        return false;
    }
    
    boolean binary_search(int[][] matrix, int row, int target){
        int[] arr = matrix[row];
        
        int start = 0;
        int end = matrix[row].length-1;
        
        while (start<=end){
            int mid = (start + end)/2;
            if (arr[mid]<target) start = mid+1;
            if (arr[mid]>target) end = mid-1;
            if (arr[mid] == target) return true;
        }
        
        return false;
    }
}