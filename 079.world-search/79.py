class Solution:
    # @param {character[][]} board
    # @param {string} word
    # @return {boolean}
    def exist(self, board, word):
        
        row_size = len(board)
        col_size = len(board[0])
        word_size = len(word)
        mask = [0] * (row_size * col_size)
        
        def dfs(row, col, phase):
            if row<0 or row>= row_size:
                return False
            if col<0 or col>= col_size:
                return False
            if mask[row * col_size + col]:
                return False
            if board[row][col] != word[phase]:
                return False
                
            if phase +1 == word_size:
                return True
                
            mask[row * col_size + col] = 1
            if dfs(row-1, col, phase+1) or dfs(row, col+1, phase+1) or dfs(row+1, col, phase+1) or dfs(row, col-1, phase+1):
                    return True
            else:
                mask[row * col_size + col] = 0
                return False
        
        
        for i in range(row_size):
            for j in range(col_size):
                r = dfs(i, j, 0)
                if r:
                    return True
                    
        return False
                
        