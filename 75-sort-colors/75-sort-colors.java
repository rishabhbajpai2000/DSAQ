class Solution {
    public void sortColors(int[] nums) {
       int[] freq = {0,0,0};
        for (int elem: nums){
            if (elem ==0) freq[0]++;
            if (elem ==1) freq[1]++;
            if (elem ==2) freq[2]++;
        }
        
        int i = 0;
        for (int j = 0; j<freq[0]; j++){
            nums[i] = 0;
            i++;
        }
        
        for (int j = 0; j<freq[1]; j++){
            nums[i] = 1;
            i++;
        }
        for (int j = 0; j<freq[2]; j++){
            nums[i] = 2;
            i++;
        }
        
    }
}