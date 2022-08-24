class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        
        def power(n):
            if (n == 2 or n == 1): return True
            if n < 2: return False
            return power(n/2)
        
        return power(n)
        