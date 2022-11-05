class Solution {
    public int climbStairs(int n) {
        
        int[] DP = new int[n+1];
        int ind = 0;
        return helper(DP, n, ind);
    }
    
    int helper(int[] DP, int n, int ind){
        if (ind == n) return 1;
        if (ind>n) return 0;
        if (DP[ind] != 0) return DP[ind];
        
        
        return DP[ind] = helper(DP, n, ind+1) + helper(DP, n, ind+2);
    }
}