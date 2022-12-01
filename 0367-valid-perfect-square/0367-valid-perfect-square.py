class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        square_root = math.sqrt(num)
        
        if square_root == int(square_root):
            return True
        return False