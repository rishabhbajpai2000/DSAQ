class Solution {
    public void reverseString(char[] s) {
        int len = s.length;
        
        for(int i = 0; i<len/2;i++){
            int first = i; 
            int second = len-1-i;
            exchange(s, first, second);
        }
        
    }
    
    void exchange(char[] s, int first, int second ){
        char temp = s[first];
        s[first] = s[second];
        s[second] = temp;
    }
}