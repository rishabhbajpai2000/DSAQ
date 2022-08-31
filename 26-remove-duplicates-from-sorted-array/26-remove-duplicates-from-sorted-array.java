class Solution {
    public int removeDuplicates(int[] nums) {
        int first = 0;
        for (int i = 0; i<nums.length; i++){
            if (nums[first] != nums[i]){
                nums[first + 1] = nums[i];
                first++;
            }
        }
        return first + 1;
    }
}