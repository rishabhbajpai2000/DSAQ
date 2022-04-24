class Solution {
    public List<Integer> intersection(int[][] nums) {
        int[] hashmap = new int[1000+1];
        
        for (int[] elem: nums){
            for(int i:elem){
                hashmap[i] += 1;
            }
        }
        
        ArrayList<Integer> ans = new ArrayList<>();
        int len = nums.length;
        for(int i = 0; i<hashmap.length; i++){
            if (hashmap[i] == len)
                ans.add(i);    
        }
        
        return ans;
        
    }
}