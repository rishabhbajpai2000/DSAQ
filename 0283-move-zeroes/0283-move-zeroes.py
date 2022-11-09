class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nonzero = []
        for i in nums:
            if i != 0:
                nonzero.append(i)
        
        c = 0
        for i in nonzero:
            nums[c] = i
            c+= 1
        
        for i in range(c, len(nums)):
            nums[i] = 0