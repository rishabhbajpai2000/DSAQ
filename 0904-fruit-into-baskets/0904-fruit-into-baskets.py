class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        ans = min(2, len(fruits))
        freq = {}
        i,j = 0,0
        while j < len(fruits):
            # increasing the window size 
            if freq.__contains__(fruits[j]): freq[fruits[j]] += 1
            else: freq[fruits[j]] = 1 
            j += 1
            
            # shrinking the window
            while len(freq) > 2:
                if freq[fruits[i]] == 1:del freq[fruits[i]]
                else: freq[fruits[i]] -= 1
                i += 1
            ans = max(ans, j-i)
        return ans 
            
            
            
        