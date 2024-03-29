class Solution {
    public int findTargetSumWays(int[] nums, int target) {
        int sum = 0;
        int ans = target(nums, target, sum, 0);
        return ans;
    }

    private static int target(int[] nums, int target, int sum, int index) {
        if (index == nums.length) {
            if (sum == target) 
                return 1;
            return 0;
        }

        return target(nums, target, sum + nums[index], index+1) + target(nums,target, sum - nums[index], index+1);
    }
    }