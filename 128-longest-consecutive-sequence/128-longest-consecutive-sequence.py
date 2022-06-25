def chain_l(s,elem):
        l = 0
        while True:
            if elem in s:
                l+= 1
                elem += 1
            else:
                return l
        return l
    
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        max_len = 0
        
        for elem in nums:
            if elem-1 not in s:
                max_len = max(max_len, chain_l(s, elem))
        
        return max_len
                
        