class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] prefix = new int[nums.length];
        int pre = 1;
        int post = 1;
        int[] postfix = new int[nums.length];
        for (int i = 0; i < nums.length; i++) {
            pre =  pre*nums[i];
            prefix[i] = pre;
        }
        for (int i = nums.length-1; i >=0; i--) {
            post = post*nums[i];
            postfix[i] =post;
        }
        
        for (int i = 0; i < nums.length; i++) {
            if (i == 0){
                nums[i] = postfix[1];
            }
            else if(i == nums.length-1){
                nums[i] = prefix[nums.length-2];
            }
            else{
            nums[i] = prefix[i-1]*postfix[i+1];
            }
        }
        return nums;
    }
}