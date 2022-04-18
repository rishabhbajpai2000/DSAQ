class Solution {
    public int strStr(String haystack, String needle) {
        if (haystack.length() == 0 && needle.length() == 0)
            return 0;
        else{
            for (int i = 0; i<haystack.length() - needle.length()+1;i++){
            String word = haystack.substring(i,i+needle.length());
            if (word.equals(needle))
                return i;
        }
        return -1;
        }
        
        
    }
}