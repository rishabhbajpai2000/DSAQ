class Solution {
    public String sortSentence(String s) {
        
        // splitting the string
        String[] a = s.split(" ");
        
        // making a string array
        String[] ans_Arr = new String[a.length];


        for(int i = 0; i<a.length; i++){

            String elem = a[i];
            String substring = a[i].substring(0, a[i].length()-1);
            char num = elem.charAt(elem.length()-1);
            int index = Character.getNumericValue(num);
            
    
            ans_Arr[index-1] = substring;
        }
        
        // making the answer string
        StringBuilder ans = new StringBuilder();
        for (int i = 0; i< ans_Arr.length;i++){
            ans.append(ans_Arr[i] + " ");
        }
        String ans_f = ans.substring(0, ans.length()-1);
        return ans_f;
        
    }
}