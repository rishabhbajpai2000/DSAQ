class Solution {
    public int missingNumber(int[] nums) {
        int n = nums.length;
        int s_t = n*(n+1)/2;
        int s = 0;
        for (int i:nums)s += i;
        return s_t - s;
    }
}