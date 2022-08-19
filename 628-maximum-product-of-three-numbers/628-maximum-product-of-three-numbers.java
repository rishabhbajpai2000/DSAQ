class Solution {
    public int maximumProduct(int[] nums) {
        // not working with negative numbers
        Arrays.sort(nums);
        int last_ind = nums.length - 1;
        int first = nums[0]*nums[1]*nums[last_ind];
        int second =  nums[last_ind] * nums[last_ind-1] * nums[last_ind-2];
        
        if (first>second) return first;
        return second;
        
        // simple brute force approach
        // int mul = nums[0]*nums[1]*nums[2];
        // for (int i = 0; i<nums.length; i++ ){
        //     for (int j = 0; j<nums.length; j++){
        //         for(int k = 0; k<nums.length; k++){
        //             if (i != j && j != k && k != i && nums[i]*nums[j]*nums[k] > mul) mul = nums[i]*nums[j]*nums[k];
        //         }
        //     }
        // }
        // return mul;
        
        // solution will be in corners 
    }
}