class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        s =set() 
        for i in nums:
            if str(i)[::-1] != str(i): 
                s.add(i)
                s.add(int(str(i)[::-1]))
            else:
                s.add(i)
        
        return len(s)
        