class Solution:
    def longestPalindrome(self, s: str) -> str:
        # return len(s)
        curmax = ""
        for start in range(len(s)):
            original = ""
            for end in range(start, len(s)):
                original = original + s[end]
                if len(curmax) < end - start + 1 and original == original[::-1]: 
                    curmax = original
                    

        return curmax
        


        
                    
            
        