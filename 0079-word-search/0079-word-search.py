class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        
        rows = len(board)
        cols = len(board[0])
        
        def helper(row, col, index):
            if index == len(word): return True
            if row == rows or col == cols  or row < 0 or col < 0: return False
            if visited[row][col] == 1: return False

            if board[row][col] != word[index]: return False
            if board[row][col] == word[index]:
                visited[row][col] = 1
                store = helper(row, col-1, index+1) or \
                       helper(row-1, col, index+1) or \
                       helper(row, col+1, index+1) or \
                       helper(row+1, col, index+1)
                visited[row][col] = -1
    
                return store
    
        
        
        for row in range(rows):
            for col in range(cols):
                visited = [[-1] * (len(board[0])) for _ in range(len(board))]
                if helper(row,col, 0): return True
        return False