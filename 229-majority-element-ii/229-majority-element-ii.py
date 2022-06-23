from collections import Counter 
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        ans = []
        f = Counter(nums)
        for i in f:
            if f[i] > len(nums)//3:
                ans.append(i) 
        return ans
        