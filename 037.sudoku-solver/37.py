
range9 = range(9)
bits = tuple( 0x01 << i for i in range9)

square0 = ((0,0), (0,1), (0,2), (1,0), (1,1), (1,2), (2,0), (2,1), (2,2))
class Solution:
    # @param {character[][]} board
    # @return {void} Do not return anything, modify board in-place instead.
    
    
    
    def square(self, index):
        base_row = (index // 3) * 3
        base_col = (index % 3) * 3
        for i in range9:
            yield (square0[i][0] + base_row, square0[i][1] + base_col)
        
    def square_by_base(self, base_row, base_col):
        for i in range9:
            yield (square0[i][0] + base_row, square0[i][1] + base_col)

    def square_by_cell(self, row, col):
        return self.square_by_base((row//3)*3, (col//3)*3)

    
    def fill_value(self, board, row, col):
        result = 0
        for i in range9:
            if board[row][i] is None:
                result += 1
        for j in range9:
            if board[j][col] is None:
                result += 1
                
        for i,j in self.square_by_base((row//3)*3, (col//3)*3):
            if board[i][j] is None:
                result += 1
        
        return result
    
    def check_row(self, board, seq):
        mask = 0
        for i in range9:
            if board[seq][i] is not None:
                b = 1 << board[seq][i] 
                if mask & b:
                    return False
                mask |=  b
            
        return True
        
    def check_col(self, board, seq):
        mask = 0
        for i in range9:
            if board[i][seq] is not None:
                b = 1 << board[i][seq] 
                if mask & b:
                    return False
                mask |= b
        return True

    def check_square(self, board, row, col):
        mask = 0
        for i,j in self.square_by_cell(row,col):
            if board[i][j] is not None:
                b = 1 << board[i][j] 
                if mask & b:
                    return False
                mask |= b
        return True
    
    def solveSudoku(self, board):

        self.result = None
    
        new_board = []
        
        def board2new(row):
            for c in row:
                if c == '.':
                    yield None
                else:
                    yield int(c)
    
        for row in board:
            new_row = list(board2new(row))
            new_board.append(new_row)

        self.dfs(new_board)

        for i in range9:
            board[i] = "".join(map(str, self.result[i]))
            
        print board

    def dfs(self, board):

        left = 0
        pick = None
        pick_value = 100
        for i in range9:
            for j in range9:
                if board[i][j] is None:
                    left += 1
                    v = self.fill_value(board, i,j)
                    if v < pick_value:
                        pick = (i,j)
                        pick_value = v

        if left == 0:
            import copy
            self.result = copy.deepcopy(board)
            return

        for i in range9:
            if self.result is not None:
                return
            board[pick[0]][pick[1]] = i + 1
            if self.check_row(board, pick[0]) and self.check_col(board, pick[1]) and self.check_square(board, pick[0],pick[1]):
                #print "try (%s, %s) with %s" % (pick[0], pick[1], i+1)
                self.dfs(board)

        board[pick[0]][pick[1]] = None
    
    
    
