class Solution {
    public int countNegatives(int[][] grid) {
        int neg = 0;
        for(int[] nums: grid){
            for(int i: nums){
                if (i<0) neg++;
            }
        }
        return neg;
    }
}