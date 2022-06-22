class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = {}
        for elem in nums:
            if elem in d.keys():
                d[elem] += 1
            else:
                d[elem] = 1
        
        l = len(nums)
        for elem in d:
            if d[elem] > l//2:
                return elem
        