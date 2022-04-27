class Solution {
    public List<Integer> findDuplicates(int[] nums) {
    ArrayList<Integer> list = new ArrayList<>();
        
        // sorting the array
        int i = 0;
        while (i<nums.length){
            int value = nums[i];
            if (i == value - 1){
                i++;
            }
            else{
                if (nums[value - 1] == value){
                    i++;
                }
                else
                    swap(nums, i, value - 1);
            }
        }
        
        
        // traversing the array to find elements which are not in their place.
        for (int j = 0; j<nums.length; j++){
            if ( j != nums[j] - 1 ){
                list.add(nums[j]);
            }
        }
        
        return list;
        
    }
    void swap(int[] arr, int first, int second){
        int temp = arr[first];
        arr[first] = arr[second];
        arr[second] = temp;
    }
}