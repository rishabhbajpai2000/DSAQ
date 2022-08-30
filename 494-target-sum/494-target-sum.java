class Solution {
    public int findTargetSumWays(int[] nums, int target) {
        int sum = 0;
        int ans = target(nums, target, sum, 0);
        return ans;
    }

    private static int target(int[] nums, int target, int sum, int i) {
        if (i == nums.length) {
            if (sum == target) 
                return 1;
            if (sum >target) return 0;
            return 0;
        }

        return target(nums, target, sum + nums[i], i+1) + target(nums,target, sum - nums[i], i+1);
    }
    }