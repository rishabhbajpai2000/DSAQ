class Solution {
    public String reverseOnlyLetters(String s) {
        char[] c = s.toCharArray();
        int start = 0;
        int end = s.length()-1;
        while (start<end){
            if (Character.isLetter(c[start]) && Character.isLetter(c[end])){
                //swapping
                char temp = c[start];
                c[start] = c[end];
                c[end] = temp;
                start++;
                end--;
            } 
            if (!Character.isLetter(c[start])) start++;
            if (!Character.isLetter(c[end])) end--;
            
            
        }
        String ans = new String(c);
        return ans;
    }
}