class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        squares = []
        squares_set = set()
        for i in range(int(math.sqrt(c)) + 1):
            if i*i<=c: 
                squares.append(i*i)
                squares_set.add(i*i)
        for i in squares:
            if c - i in squares_set: 
                return True
        return False