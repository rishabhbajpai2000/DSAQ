class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        s_t = n*(n+1)//2
        s_a = sum(nums)
        
        return s_t - s_a