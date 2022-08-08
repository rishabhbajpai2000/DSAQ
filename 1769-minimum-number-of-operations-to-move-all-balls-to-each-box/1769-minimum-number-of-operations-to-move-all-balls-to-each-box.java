class Solution {
    
    public int[] minOperations(String boxes) {
        int len = boxes.length();
        int[] ans = new int[len];
        int sum = 0;
        for (int i = 0; i<len;i++){
            // for integers from 0 to i
            sum = 0;
            for (int j = 0; j<i;j++){
                if (boxes.charAt(j) == '1') sum += i - j; 
            }
            ans[i] += sum;
            // for intgers from i to n
            sum = 0;
            for (int j = i; j<len; j++){
                if (boxes.charAt(j) == '1') sum += j-i; 
            }
            ans[i] += sum;
        }
        
        return ans;
    }
}