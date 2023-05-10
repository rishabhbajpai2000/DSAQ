def createMatrix(n):
    return [[0]*n for _ in range(n)]


def printMatrix(matrix):
    for row in matrix:
        print(row)
counter = 1

def insert_outer(UL, UR, LL, LR, matrix):
    global counter
    #upper row
    for col in range(UL, UR):
        matrix[UL][col] = counter 
        counter += 1

    #Right most column 
    for row in range(UL, LL):
        matrix[row][UR] = counter
        counter += 1

    #lower row from right to left
    for col in range(UR, UL, -1):
        matrix[LL][col] = counter
        counter += 1

    #left column
    for row in range(LL, UL, -1):
        matrix[row][UL] = counter
        counter += 1
        
    return matrix

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        global counter
        matrix = createMatrix(n)

        size = len(matrix)
        outer_peri = size-1
        for i in range(outer_peri//2 + 1):
            matrix = insert_outer(UL=i, UR=outer_peri-i, LL=outer_peri -
                        i, LR=outer_peri-i, matrix=matrix)
        if size % 2 == 1:
            matrix[size//2][size//2] = counter
        counter = 1
        return matrix