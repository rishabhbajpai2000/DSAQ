class Solution:
    def minLength(self, s: str) -> int:
        sb = list(s)
        i = 0
        while i < len(sb) - 1:
            if sb[i] == 'A' and sb[i+1] == 'B':
                del sb[i:i+2]
                i = max(0, i-1)
            elif sb[i] == 'C' and sb[i+1] == 'D':
                del sb[i:i+2]
                i = max(0, i-1)
            else:
                i += 1
        return len(sb)