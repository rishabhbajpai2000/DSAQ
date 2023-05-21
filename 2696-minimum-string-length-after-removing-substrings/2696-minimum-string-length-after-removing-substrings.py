class Solution:
    def minLength(self, s: str) -> int:
        while s.count("AB") >  0 or s.count("CD") > 0:
            first = max(s.find("AB"), s.find("CD"))
            s = s[:first] + s[first+2:]
        return len(s)