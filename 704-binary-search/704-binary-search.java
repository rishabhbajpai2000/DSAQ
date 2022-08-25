class Solution {
    public int search(int[] nums, int target) {
        return bin(nums, target, 0, nums.length-1);
    }
    static int bin(int[] nums, int target, int start, int end){
        int mid = (start + end)/2;
        int elem = nums[mid];
        if (start > end) return -1;
        if (elem == target) return mid;
        if (elem>target) return bin(nums, target, start, mid-1);
        return bin(nums, target, mid + 1, end);
        

    }
}