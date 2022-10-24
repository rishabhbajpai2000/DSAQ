class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        
        freq = {}
        for i in arr1:
            if freq.__contains__(i):
                freq[i] += 1
            else: freq[i] = 1
        ans = []
        for i in arr2:
            repetetion = freq[i]
            for p in range(repetetion):
                ans.append(i)
            del freq[i]
       
        l = len(ans)
        for i in freq:
            repetetion = freq[i]
            for p in range(repetetion):
                ans.append(i)
        
        ans[l: ] = sorted(ans[l:])
        return ans