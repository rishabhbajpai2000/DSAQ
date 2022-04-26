class Solution {
    public String longestCommonPrefix(String[] strs) {
        
        int k = 0;
        // find the length of the shortest string in the array. 
        int minl = strs[0].length();
        String min = strs[0];
        for (String elem: strs){
            if (elem.length()<minl){
                minl = elem.length();
                min = elem;
            }
        }
        
        // outer loop will run only those number of times. 
        for (int i = 0; i<minl; i++){
            char c = strs[0].charAt(i);
            for(String elem:strs){
                if (elem.charAt(i) != c){
                    return elem.substring(0, i);
                }
            }
        }
        return min;
    }
}