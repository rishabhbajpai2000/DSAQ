class Solution {
    public int minCostClimbingStairs(int[] cost) {
        int[] dp = new int[cost.length];
        Arrays.fill(dp, -1);
        return Math.min(helper(0, dp, cost) , helper(1, dp, cost));
    }
    
    int helper(int ind, int[] dp, int[] cost){
        if (ind > cost.length)
            return 1000_000_000;
        if (ind == cost.length) return 0;
        if (ind == cost.length-1) return cost[ind];
        if (dp[ind] != -1) return dp[ind];
        
        return dp[ind] = cost[ind] +  Math.min(helper(ind+1, dp, cost), helper(ind+2, dp, cost));
    }
}