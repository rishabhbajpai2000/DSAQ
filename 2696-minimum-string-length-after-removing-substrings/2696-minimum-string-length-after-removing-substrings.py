class Solution:
    def minLength(self, s: str) -> int:
        # start = 0
        # while start<len(s)-1:
        #     print(s)
        #     if s[start:start + 1] in ["AB", "CD"]:
        #         s = s[:start-1] + s[start+2: ]
        #     start += 1
        # return len(s)
    
        while s.count("AB") >  0 or s.count("CD") > 0:
            first = max(s.find("AB"), s.find("CD"))
            s = s[:first] + s[first+2:]
        return len(s)