class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq = {}
        for i in s:
            if freq.__contains__(i):
                freq[i] += 1
            else:
                freq[i] = 1
                
        for i in range(len(s)):
            if freq[s[i]] == 1:
                return i
        return -1