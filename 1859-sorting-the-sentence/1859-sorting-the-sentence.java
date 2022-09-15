class Solution {
    public String sortSentence(String s) {

        int l = s.length();
        String arr[] = s.split(" ");
        String ans[]=new String[arr.length];
            
        for (int i = 0; i < arr.length; i++) {
            String words = arr[i];
            int len = words.length();
            ans[Character.getNumericValue(words.charAt(len - 1))-1] = words.substring(0, len-1);

        }
        String str = "";
        for (int i = 0; i < ans.length; i++) {
            str = str + ans[i] + " ";
        }
        return str.substring(0, str.length()-1);
    }
}
