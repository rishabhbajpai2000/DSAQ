class Solution {
    public int searchInsert(int[] nums, int target) {
        
        int ans = Arrays.binarySearch(nums, target);
        if (ans>=0) return ans;
        else return -1*ans - 1;
    }
}