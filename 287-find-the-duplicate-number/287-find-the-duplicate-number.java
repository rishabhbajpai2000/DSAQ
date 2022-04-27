class Solution {
static int findDuplicate(int[] nums) {
        int i = 0;
        while (i<nums.length){
            int val = nums[i];
            if (i == val - 1){
                i++;
            } 
            else{
                if (nums[val-1] == val){
                    return val;
                }
                else{
                    // System.out.println("before" + Arrays.toString(nums));
                    swap(nums, i, val-1);
                    // System.out.println("After: " + Arrays.toString(nums));
                }
            }
        }
        return -1;
    }

    
    static void swap(int[] arr, int first, int second){
        int temp = arr[first];
        arr[first] = arr[second];
        arr[second] = temp;
    }
}