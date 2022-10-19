class Solution:
    def greatestLetter(self, s: str) -> str:
        s = set(s)
        maxi = ""
        for i in s:
            # checking for the lower letters
            if i.islower() and i.upper() in s:
                maxi = max(maxi, i.upper())
            
            if i.isupper() and i.lower() in s:
                maxi = max(maxi, i)
                
        return maxi
                