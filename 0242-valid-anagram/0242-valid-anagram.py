class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq1 = Counter(s)
        freq2 = Counter(t)
        for i in freq1:
            if freq1[i] != freq2[i]: return False
        for i in freq2:
            if freq1[i] != freq2[i]: return False
        return True