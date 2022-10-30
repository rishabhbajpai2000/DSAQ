def issafe(board, row, col):
    # checking the column 
    for r in range(row):
        if board[r][col]: return False 
    
    maxleft = min(row, col)
    # checking left diagonal
    for i in range(1, maxleft+1):
        if board[row-i][col-i]: return False

    # checking right diagonal 
    maxright = min(row, len(board)-col-1)
    for k in range(1, maxright+1):
        if board[row-k][col+k]: return False

    return True
     
def format(board):
    b = []
    for row in board:
        l = ""
        for elem in row:
            if elem == False: l += "."
            else: l+= "Q"
        b.append(l)
    return b
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = []
        for i in range(n):
            local = []
            for i in range(n):
                local.append(False)
            board.append(local)
        answers = []
        
        def helper(board, row):
            if row == len(board):
                answers.append(format(board))
                return 

            for col in range(len(board)):
                if issafe(board, row, col):
                    board[row][col] = True
                    helper(board=board,row=row+1)
                    board[row][col] = False
        
        helper(board, 0)
        return answers