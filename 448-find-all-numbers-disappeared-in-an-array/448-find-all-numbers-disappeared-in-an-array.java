class Solution {
    public List<Integer> findDisappearedNumbers(int[] nums) {
        // from the length of the nums
        // make a second boolean array of len n, 
        // then mark the elements and return which r not found 
        int[] sec = new int[nums.length + 1];
        for(int elem: nums) sec[elem] = 1;
        
        List<Integer> list = new ArrayList<>();
        for (int i = 1; i<sec.length; i++){
            if (sec[i] != 1) list.add(i);
        }
        return list;
        
        // follow up 
        // we can use cycle sort to sort the array and we will get our culprit in n time 
    }
}