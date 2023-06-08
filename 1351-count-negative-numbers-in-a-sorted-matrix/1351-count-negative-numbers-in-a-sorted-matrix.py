class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        negatives = 0
        for row in grid:
            for elem in row:
                if elem<0: negatives += 1
        return negatives