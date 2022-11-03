class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        ab = s+s
        ab = ab[1:-1]
        if s in ab:
            return True
        return False