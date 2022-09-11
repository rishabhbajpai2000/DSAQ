class Solution:
    def partitionString(self, s: str) -> int:
        start = 0
        count = 1
        for i in range(len(s)):
            if s[i] in s[start:i]:
                count += 1
                start = i
        
        return count
        