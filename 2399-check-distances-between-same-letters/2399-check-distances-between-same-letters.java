class Solution {
    public boolean checkDistances(String s, int[] distance) {
        int[] check = new int[26];
        int[] occurance = new int[26];
        // for (int i = 0; i<26; i++) check[i] = -1;
        
        for(int i = 0; i<s.length(); i++){
            char c = s.charAt(i);
            int pos_in_check = c-'a';
            if (check[pos_in_check] == 0){
                check[pos_in_check] = -(i + 1);                         
                occurance[pos_in_check] = -1;
            }
            else check[pos_in_check] += i;
        }
        System.out.println(Arrays.toString(check));
        for(int i = 0; i<check.length; i++)
            if (occurance[i] == -1 && check[i] != distance[i]) return false;
        return true;
    }
}