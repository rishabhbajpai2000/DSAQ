class Solution {
    public boolean judgeCircle(String moves) {
        
        char[] chars = moves.toCharArray();
        
		//No need to loop if the number of steps are odd
        if((chars.length & 1) == 1) return false;
        
        char[] result = new char[26];
        for(char c: chars) {
            result[c-'A']++;
        }
        
        return result['R'-'A'] == result['L'-'A'] && result['U'-'A'] == result['D'-'A'];
    }
}