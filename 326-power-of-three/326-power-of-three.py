class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def power(n):
            if (n == 3 or n == 1): return True
            if n < 9: return False
            if n %3 == 0:
                return power(n/3)
            return False
        
        return power(n)