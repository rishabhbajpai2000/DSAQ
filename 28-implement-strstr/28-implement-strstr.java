class Solution {
    public int strStr(String haystack, String needle) {
        int l1=haystack.length();//5
        int l2=needle.length();//3
        int c=0;
        for(int i=0;i<l1-l2+1;i++){
           String sub=haystack.substring(i,i+l2); 
            if(sub.equals(needle))
                return i;
        }
        return -1;
    }
}