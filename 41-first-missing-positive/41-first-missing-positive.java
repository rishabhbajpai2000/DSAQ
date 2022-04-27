class Solution {
    public int firstMissingPositive(int[] nums) {
        int i, n = nums.length;
        
        for(i=0; i<n; i++){
           if((i+1) != nums[i]){
               if(nums[i]<1 || nums[i]>n || nums[i] == nums[nums[i]-1]) continue;
               else{
                   int t = nums[nums[i]-1];
                   nums[nums[i]-1] = nums[i];
                   nums[i] = t;
                   i--;
               }
           }
        }
        
        for(i=0; i<n && (i+1 == nums[i]); i++);
        
        return i+1;
    }
}