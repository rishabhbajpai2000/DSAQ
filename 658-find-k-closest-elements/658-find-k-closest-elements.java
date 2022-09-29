class Solution {
    public List<Integer> findClosestElements(int[] arr, int k, int x) {
        int first = 0;
        int last = arr.length-1;
        
        while (last - first + 1 != k){
            if (arr[last] - x >= x-arr[first]) last--;
            else first++;
        }
        
        List<Integer> ans = new ArrayList<Integer>();
        for (int i = first;i<= last; i++){
            ans.add(arr[i]);
        }
        
        return ans;
    }
}