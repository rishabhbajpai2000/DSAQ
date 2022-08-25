class Solution {
    public void reverseString(char[] s) {
        int len = s.length;
        reverse(s, 0, len-1);

        
    }
    
    static void reverse(char[] arr, int start, int end){
        if (start>end) return;
        exchange(arr, start, end);
        reverse(arr, start+1, end-1);
    }
    static void exchange(char[] s, int first, int second ){
        char temp = s[first];
        s[first] = s[second];
        s[second] = temp;
    }
}