class Solution {
    public int[] countPoints(int[][] points, int[][] queries) {
        int[] ans = new int[queries.length];
        
        int counter = 0;
        for (int[] circle: queries){
            int sum = 0;
            for (int[] point: points){
                int xc = circle[0];
                int yc = circle[1];
                int rc = circle[2];
                
                int x = point[0];
                int y = point[1];
                
                if ((x - xc)*(x-xc) + (y-yc)*(y-yc) <= rc*rc) sum++;
            }
            ans[counter] = sum;
            counter+= 1;

        }
        
        return ans;
        
    }
}