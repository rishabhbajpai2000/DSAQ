class Solution:
    def reverse(self, x: int) -> int:
        if x == 0: return 0
        if x>0:
            sol = int(str(x)[::-1])
        else:
            newint = str(x)[1:]
            sol = int("-" + str(newint)[::-1])
        if sol > (2 ** 31) - 1 or sol < -(2**31): return 0
        
        return sol