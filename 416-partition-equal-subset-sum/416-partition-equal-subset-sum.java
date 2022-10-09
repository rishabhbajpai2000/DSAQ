class Solution {
    public boolean canPartition(int[] nums) {
        int s = 0;
        for (int elem:nums)s+= elem;
        if (s%2 != 0) return false;
        
        int[][] dp = new int[nums.length][s/2 + 1];
        for(int[] arr:dp) Arrays.fill(arr, -1);
        
        return subsetSumUtil(nums.length-1, s/2, nums, dp);
    }
    
     boolean subsetSumUtil(int ind, int target, int[] arr, int[][] dp) {
        if (target == 0)
            return true;
        if (ind == 0)
            return arr[0] == target;
        if (dp[ind][target] != -1)
            return dp[ind][target] == 0 ? false : true;
        boolean notTaken = subsetSumUtil(ind - 1, target, arr, dp);
        boolean taken = false;
        if (arr[ind] <= target)
            taken = subsetSumUtil(ind - 1, target - arr[ind], arr, dp);
        dp[ind][target] = notTaken || taken ? 1 : 0;
        return notTaken || taken;
    }
}