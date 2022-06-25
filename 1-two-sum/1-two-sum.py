class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = {}
        for i in range(len(nums)):
            if ans.__contains__(target - nums[i]):
                return [i, ans[target-nums[i]]]
            else:
                ans[nums[i]] = i
        
        