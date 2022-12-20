class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:

        increment = 0
        decrement = len(arr)-1
        
        while increment < len(arr)-1 and arr[increment+1] > arr[increment] : increment += 1
        while decrement > 0 and arr[decrement-1] > arr[decrement]: decrement -= 1 
        
        
        if 0 < increment == decrement < len(arr)-1: return True
        return False