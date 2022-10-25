class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        
        
        def helper(index, current, s ):
            if s == target:
                result.append(current.copy())
                return 
            if s > target or index >= len(candidates):
                return 
            
            # first decision - 2,2,2,2,2,2...........
            
            current.append(candidates[index])
            helper(index, current, s + candidates[index])
            current.pop()
            
            # second decision
            helper(index + 1, current, s)
            
        helper(0, [], 0)
        return result