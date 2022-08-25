class Solution {
    public List<String> letterCombinations(String digits) {
        
        if( digits.equals("")){
            List<String> l = new ArrayList<>();
            return l;
        }
        list = new ArrayList<>();
        combinations("", digits);
        return list;
    }
    
     static List<String> list = new ArrayList<>();    
     static void combinations(String pr, String unpr) {

        if (unpr.isEmpty()) {
            list.add(pr);
            return;
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

        for (int i = 0; i < phone[num - 2].length; i++) {
            String ch =  phone[num-2][i];
            combinations(pr + ch, unpr.substring(1));
        }
    }
}