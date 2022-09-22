class Solution {
    public String reverseVowels(String s) {
        
        int i = 0;
        int j = s.length()-1;
        
        char[] arr = s.toCharArray();
        
        HashSet<Character> set = new HashSet<>();
        char[] c = {'a','e','i','o','u','A','E','I','O','U'};
        for(char ch:c) set.add(ch);

        
        while(i<j){
            if(set.contains(arr[i])&&set.contains(arr[j])){
                char temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
                i++;
                j--;
            }
            else if(set.contains(arr[i])) j--;
            else i++;
        }
        
        
        String ans = new String(arr);
        return ans;
    }
}