class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        max_len = 0
        
        for elem in nums:
            if elem-1 not in s:
                length = 0
                while (elem+length) in s:
                    length+=1
                max_len = max(max_len,length)
        
        return max_len
                
        