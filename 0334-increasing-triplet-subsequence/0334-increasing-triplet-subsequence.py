class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        max1 = max(nums) +1
        max2 = max(nums) +1
        if len(nums)<3: return False
        
        for i in nums:
            if i <= max1:
                max1 = i
            elif i <= max2:
                max2 = i
            else:
                return True
        return False
        
        