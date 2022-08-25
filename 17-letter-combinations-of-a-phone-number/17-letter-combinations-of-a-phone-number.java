class Solution {
    public List<String> letterCombinations(String digits) {
        if( digits.equals("")){
            List<String> l = new ArrayList<>();
            return l;
        }
        return combinations("",digits);
    }
    
    List<String> combinations(String pr, String unpr) {

        if (unpr.isEmpty()) {
            List<String> list = new ArrayList<>();
            list.add(pr);
            return list;
        }
        String[][] phone = {
                { "a", "b", "c" },
                {"d","e","f"},
                { "g", "h", "i" },
                { "j", "k", "l" },
                { "m", "n", "o" },
                { "p", "q", "r", "s" },
                { "t", "u", "v" },
                { "w", "x", "y", "z" } };

        int num = unpr.charAt(0) - '0';

        List<String> list = new ArrayList<>();
        for (int i = 0; i < phone[num - 2].length; i++) {
            String ch =  phone[num-2][i];
            list.addAll(combinations(pr + ch, unpr.substring(1)));
        }
        return list;
    } 
}