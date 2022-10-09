class Solution {
public:
    long long mod = 1e9+7;
    int memo(vector<vector<int>>& a,int i,int j,int sum,int k,vector<vector<vector<int>>>& dp){
        if(i<0 || j<0)
            return 0;
        if(i==0 && j==0){
            sum+=a[0][0];
            return sum%k==0;
        }
        
        if(dp[i][j][sum%k]!=-1)
            return dp[i][j][sum%k];
        
        int left = memo(a,i,j-1,(sum+a[i][j])%k,k,dp)%mod;
        int right = memo(a,i-1,j,(sum+a[i][j])%k,k,dp)%mod;
        return dp[i][j][sum%k] = (left+right)%mod;
        
    }
    int numberOfPaths(vector<vector<int>>& grid, int k) {
        
        int m = size(grid),n=size(grid[0]);
        vector<vector<vector<int>>> dp(m,vector<vector<int>>(n,vector<int>(51,-1)));

        return memo(grid,m-1,n-1,0,k,dp);
    }
};