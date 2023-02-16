class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        presum = 0
        prosum = sum(nums) 
        for index,elem in enumerate(nums):
            prosum -= elem
            if presum == prosum: return index
            presum += elem
        return -1