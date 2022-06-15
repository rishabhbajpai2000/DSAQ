class Solution {
    public int[] intersection(int[] nums1, int[] nums2) {
        
        Set<Integer> intersect = new HashSet<Integer>();
        
        for (int elem: nums1){
            if (check(nums2, elem))
                intersect.add(elem);
        }
        
        int n = intersect.size();
        int ans[] = new int[n];
        
        int i = 0;
        for (int x : intersect)
            ans[i++] = x;
        
        return ans;
    }
    static boolean check(int[] arr, int i){
        for (int elem:arr){
            if (elem == i)
                return true;
        }
        return false;
    }
}