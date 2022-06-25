class Solution {
    public int uniquePaths(int m, int n) {
        // making a two d array, initially it will be filled with zeroes all along 
        int[][] arr = new int[m+1][n+1];
        // last row last column is made 1
        arr[0][0] = 1;
        arr[m-1][n-1] = 1;
        // now we need to traverse the array and fill in the values.
        for (int i = m-1; i>-1; i--){
            for (int j = n-1; j>-1; j--){
                if (i == m-1 && j == n-1) continue;
                arr[i][j] = arr[i][j+1] + arr[i+1][j];
            }
        }
        
        return arr[0][0];
    }
}