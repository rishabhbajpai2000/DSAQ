class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        s_t = n*(n+1)//2
        s_a = 0
        for i in nums: s_a += i
        
        return s_t - s_a