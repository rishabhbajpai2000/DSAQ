class Solution {
    public int maxProduct(int[] nums) {
        Arrays.sort(nums);
        int largest = nums[nums.length -1];
        int secondlargest = nums[nums.length -2];
        return (largest-1) * (secondlargest-1);
    }
}