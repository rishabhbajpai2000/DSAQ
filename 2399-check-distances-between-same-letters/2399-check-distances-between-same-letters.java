class Solution {
    public boolean checkDistances(String s, int[] distance) {
        int[] check = new int[26+26];

        // for (int i = 0; i<26; i++) check[i] = -1;
        
        for(int i = 0; i<s.length(); i++){
            char c = s.charAt(i);
            int pos_in_check = c-'a';
            if (check[pos_in_check] == 0){
                check[pos_in_check] = -(i + 1);                         
                check[pos_in_check + 26] = -1;
            }
            else check[pos_in_check] += i;
        }
        for(int i = 0; i<26; i++)
            if (check[i+26] == -1 && check[i] != distance[i]) return false;
        return true;
    }
}