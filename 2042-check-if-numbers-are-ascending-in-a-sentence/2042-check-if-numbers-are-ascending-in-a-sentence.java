class Solution {
    public boolean areNumbersAscending(String s) {;
        int c = 0;
        String[] sp = s.split(" ");
        ArrayList<Integer> nums = new ArrayList<Integer>();
        
        for(String str: sp){
            if (isNumeric(str)) nums.add(Integer.parseInt(str)); 
        }
        
        int l = nums.size();
        for (int i = 0; i < l-1; i++) {
            if (nums.get(i) >= nums.get(i + 1))
                return false;
        }
        return true;
    }
    
    static boolean isNumeric(String str) {
        return str.matches("-?\\d+(\\.\\d+)?");  //match a number with optional '-' and decimal.
    }
}