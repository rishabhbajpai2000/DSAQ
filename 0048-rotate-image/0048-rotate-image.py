class Solution:
    
    def swap(self, matrix, first, second):
        for row in range(len(matrix)):
            matrix[row][first], matrix[row][second] = matrix[row][second], matrix[row][first]

    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # first take transpose
        for row in range(len(matrix)):
            for col in range(row):
                matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]
                
        
        # then interchange the cols like first and last,
        cols =  len(matrix[0])
        for col in range(cols//2):
            self.swap(matrix, col, cols-col-1)
        