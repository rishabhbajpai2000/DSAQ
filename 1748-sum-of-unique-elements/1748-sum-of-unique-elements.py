class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        dic = {}
        for i in nums:
            if dic.__contains__(i): dic[i] += 1
            else: dic[i] = 1
        
        s = 0
        for i in dic:
            if dic[i] == 1: s+= i
                
        return s
        