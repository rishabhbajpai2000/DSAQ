class Solution {
    public int majorityElement(int[] nums) {
        int m = 0;
        int c = 0;
        
        for (int elem: nums){
            if (c==0){
                m = elem;}
            if (elem == m){
                c++;}
            else
            {c--;}
        }
        
        return m;
        
        
    }
}