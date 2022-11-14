class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        distinct = set()
        
        def helper(nums):
            if len(nums) == 0:
                return
            
            m = min(nums)
            M = max(nums)
            
            nums.remove(m)
            nums.remove(M)
            
            av = (M + m)/2
            
            distinct.add(av)
            helper(nums)
        
        helper(nums)
        return len(distinct)