class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        prefix = []
        s = set()
        for i in nums:
            s.add(i)
            prefix.append(len(s))
            
        s = set()
        suffix = []
        for i in range(len(nums)-1,0,-1): 
            s.add(nums[i])
            suffix.insert(0,len(s))
        suffix.append(0)
        
        print("prefix", prefix)
        print("suffix", suffix)
        
        answer = []
        for i in range(len(prefix)):
            answer.append(prefix[i] - suffix[i])
        
        return answer