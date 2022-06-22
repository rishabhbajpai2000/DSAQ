class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        m, c = 0,0
        for elem in nums:
            if (c == 0):
                m = elem
                
            if elem == m:
                c += 1
            else:
                c -= 1
            

        return m
            
        