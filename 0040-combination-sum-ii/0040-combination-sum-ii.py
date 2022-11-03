class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()
        
        def helper(index, current, s ):
            if s == target:
                result.append(current.copy())
                return 
            if s > target or index >= len(candidates):
                return 
            
            # first decision - taking
            
            current.append(candidates[index])
            helper(index+1, current, s + candidates[index])
            current.pop()
            
            # second decision - move forward
            while (index < len(candidates)-1 and candidates[index] == candidates[index+1] ):
                index+= 1
            helper(index + 1, current, s)
            
        helper(0, [], 0)
        return result