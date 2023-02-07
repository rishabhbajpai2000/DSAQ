class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        positions = {}
        for i in range(len(nums)):
            if positions.__contains__(target - nums[i]): 
                return [i, positions[target-nums[i]]]
            else: 
                positions[nums[i]] = i