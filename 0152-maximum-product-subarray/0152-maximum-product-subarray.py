class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        res = nums[0]
        curmin, curmax = 1,1
        
        for n in nums:
            tmp = curmax*n
            curmax = max(tmp, curmin*n, n)
            curmin = min(tmp, curmin*n, n)
            
            res = max(curmax, res)
        
        return res