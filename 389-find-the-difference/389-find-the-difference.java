class Solution {
    public char findTheDifference(String s, String t) {
        int[] s_freq = new int[26];
        int [] t_freq = new int[26];
        
        for (int i = 0; i<s.length(); i++){
            s_freq[s.charAt(i) - 'a']++;
        }
        
        for (int i = 0; i<t.length(); i++){
            t_freq[t.charAt(i) - 'a']++;
        }
        
        for(int i = 0; i<26; i++){
            if (s_freq[i] != t_freq[i]) return (char)('a' + i);
        }
        
        return 'a';
    }
}