class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int i = m-1; // first array last index with non zero element
        int j = n-1; // second array last index
        int k = m+n-1; // first array's last index
        
        while (i>=0 && j>=0){
            int first = nums1[i];
            int second = nums2[j];
            if (first>second){
                nums1[k] = first;
                i--;
            }
            else{
                nums1[k] = second;
                j--;
            }
            k--;
        }
        while (j>=0){
            nums1[k] = nums2[j];
            k--;
            j--;
        }
    }
    
}