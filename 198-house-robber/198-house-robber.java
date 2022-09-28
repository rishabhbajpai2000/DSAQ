class Solution {
    public int rob(int[] nums) {
        int[] dp = new int[nums.length];
        for (int i = 0;i<nums.length;i++)dp[i] = -1;
        return f(nums, nums.length-1, dp);
    }
    
    int f(int[] nums, int i, int[] dp){
        if (i == 0) return nums[i];
        if (i<0) return 0;
        if (dp[i] != -1) return dp[i];
        int chosen = nums[i] + f(nums, i-2, dp);
            int not_chosen = f(nums, i-1, dp);
        
        return dp[i] = Math.max(chosen, not_chosen);
    }
}