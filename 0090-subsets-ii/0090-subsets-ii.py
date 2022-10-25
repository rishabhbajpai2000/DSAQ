class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        results = []
        nums.sort()
        
        def subsets(index, current):
            if index == len(nums):
                if current in results:
                    return 
                else:
                    results.append(current.copy())
                    return 
            
            current.append(nums[index])
            subsets(index+1, current)
            current.pop()
            
            while index+1<len(nums) and nums[index] == nums[index+1]:
                index+=1
            subsets(index+1, current)
       
        subsets(0, [])
        return results