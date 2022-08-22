class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        s =set(arr)
        for i in arr:
            if i/2 in s and i != 0:
                return True
            
            if i == 0:
                count = 0
                for i in arr:
                    if i == 0: count += 1
                if count == 2: return True
                    
        return False