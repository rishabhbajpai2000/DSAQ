class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        dic = {}
        for i in nums:
            if dic.__contains__(i):
                dic[i] += 1
            else:
                dic[i] = 1
        
        ans = [0,0]
        for i in dic:
            if dic[i] % 2 == 0:
                ans[0] += dic[i]//2
            else: 
                ans[0] += dic[i]//2
                ans[1] += 1
        return ans
                
        