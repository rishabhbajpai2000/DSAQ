class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def power(n):
            if (n == 4 or n == 1): return True
            if n < 4: return False
            if n %4 == 0:
                return power(n/4)
            return False
        
        return power(n) 