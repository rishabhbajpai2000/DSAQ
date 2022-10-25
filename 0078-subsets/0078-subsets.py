class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        results = []
        
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
            
            subsets(index+1, current)
       
        subsets(0, [])
        return results