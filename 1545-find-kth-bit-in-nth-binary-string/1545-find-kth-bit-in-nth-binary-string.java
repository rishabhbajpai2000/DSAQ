class Solution {
        public char findKthBit(int n, int k) {
        String[] strs = new String[n];
        strs[0] = "0";
        for(int i = 1; i<n; i++)
            strs[i] = formString(strs[i-1]);
        
        return strs[n-1].charAt(k-1);
    }

    private static String formString(String str){
        return str + "1" + reverse(invert(str));    
    }
    
    
    private static String reverse(String str) {
        return new StringBuilder(str).reverse().toString();
    }

    private static String invert(String str) {

        StringBuilder sb = new StringBuilder();
        for(char c: str.toCharArray()){
            if (c=='1') sb.append('0');
            else sb.append('1');
        }
        
        return sb.toString();
    }
}