class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        
        ans = 0
        for index in range(0,len(nums)):
            if index == 0 and nums[index] == 0:
                start = index
                while start < len(nums) and nums[start] == 0: start += 1
                count = start - index
                ans += count*(count+1)//2
                
            elif nums[index] == 0 and nums[index-1] != 0:
                start = index
                while start < len(nums) and nums[start] == 0: start += 1
                count = start - index
                ans += count*(count+1)//2

        return ans
            