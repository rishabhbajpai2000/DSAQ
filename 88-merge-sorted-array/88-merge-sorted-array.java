class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        //solution 1
        if (n == 0) return;
        if (m == 0 && n==1) nums1[0] = nums2[0]; 
        
        for (int i = m; i<m+n; i++)
            nums1[i] = nums2[i-m];
        
        
        Arrays.sort(nums1);
        
    }
}