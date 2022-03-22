class Solution {
    public void rotate(int[] nums, int k) {
        // making a copy of the old array
        int[] copy = new int[nums.length];
        for(int i = 0; i<nums.length; i++)  {
            copy[i] = nums[i];
        }
        for(int i = 0; i<nums.length; i++)  {
            int new_pos = (i+k)%nums.length;
            nums[new_pos] = copy[i];
        }
        
    }
}