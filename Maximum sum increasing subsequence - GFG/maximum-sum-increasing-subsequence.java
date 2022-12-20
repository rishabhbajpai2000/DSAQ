//{ Driver Code Starts
//Initial Template for Java

import java.io.*;
import java.util.*;
class GfG
{
    public static void main(String args[])
        {
            Scanner sc = new Scanner(System.in);
            int t = sc.nextInt();
            while(t-->0)
                {
                    int n = sc.nextInt();
                    int Arr[] = new int[n];
                    for(int i = 0;i<n;i++)
                        Arr[i] = sc.nextInt();
                    Solution ob = new Solution();
                    System.out.println(ob.maxSumIS(Arr,n));
                }
        }
}    
// } Driver Code Ends


//User function Template for Java

class Solution
{
	public int maxSumIS(int arr[], int n)  
	{  
	    return lengthOfLIS(arr);
	}  
	int lengthOfLIS(int[] arr) {
        int n = arr.length;
        int dp[][]=new int[n][n+1];
        for(int row[]: dp)
        Arrays.fill(row,-1);

        return getAns(arr,n,0,-1,dp);
    }
    int getAns(int arr[], int n,  int ind, int prev_index,int[][] dp){
    
    // base condition
    if(ind == n)
        return 0;
        
    if(dp[ind][prev_index+1]!=-1)
        return dp[ind][prev_index+1];
    
    int notTake = 0 + getAns(arr,n,ind+1,prev_index,dp);
    
    int take = 0;
    
    if(prev_index == -1 || arr[ind] > arr[prev_index]){
        take = arr[ind] + getAns(arr,n,ind+1,ind,dp);
    }
    
    return dp[ind][prev_index+1] = Math.max(notTake,take);
}
}