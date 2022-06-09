class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int[] arr = new int[2]; 
        int l = 0;
        int r = numbers.length-1;
        while (r>l){
            int cursum = numbers[r]+ numbers[l];
            if (cursum > target)
                r--;
            
            else if(cursum < target)
                l++;
            
            else{
                arr[0] = l+1;
                arr[1] = r+1;
                return arr;
            }
                
        }
        return arr;
        
    }
}