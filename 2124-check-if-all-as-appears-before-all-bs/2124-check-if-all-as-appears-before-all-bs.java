class Solution {
    public boolean checkString(String s) {
        int first_b = s.length()-1;
        int last_a = 0;
        
        for (int i =0; i<s.length(); i++){
            if (s.charAt(i) == 'a') last_a = i;
        }
        
        for (int i = 0; i<s.length(); i++){
            if (s.charAt(i) == 'b') {
                first_b = i;
                break;
            }
            
        }
        if (last_a>first_b) return false;
        return true;
    }
}