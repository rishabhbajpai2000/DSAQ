class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int m = nums1.length;
        int n = nums2.length;
        int[] merged = new int[m+n];
        int i = m-1; // first array last index with non zero element
        int j = n-1; // second array last index
        int k = m+n-1; // merged array's last index
        
        // making a new merged array 
        while (i>=0 && j>=0){
            int first = nums1[i];
            int second = nums2[j];
            if (first>second){
                merged[k] = first;
                i--;
            }
            else{
                merged[k] = second;
                j--;
            }
            k--;
        }
        while (j>=0){
            merged[k] = nums2[j];
            k--;
            j--;
        }
        while (i>=0){
            merged[k] = nums1[i];
            k--;
            i--;
        }
        
        
        int len = merged.length;
        k = len -1;
        double median = 0;
        if (len%2 == 0){
            median = (merged[k/2] + merged[k/2 + 1]);
            median /= 2;
            return median;
        }
        else{
            median = merged[k/2];
            return median;
        }
    }
}