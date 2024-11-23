class GomokuGame:
    def check_winner(self):
        # Check horizontal lines
        for row in self.board:
            for i in range(len(row) - 4):
                if row[i] == row[i+1] == row[i+2] == row[i+3] == row[i+4]:
                    return self.current_player
    
        # Check vertical lines
        for col in range(len(self.board[0])):
            for i in range(len(self.board) - 4):
                if self.board[i][col] == self.board[i+1][col] == self.board[i+2][col] == self.board[i+3][col] == self.board[i+4][col]:
                    return self.current_player
    
        # Check diagonal lines (top-left to bottom-right)
        for row in range(len(self.board) - 4):
            for col in range(len(self.board[0]) - 4):
                if self.board[row][col] == self.board[row+1][col+1] == self.board[row+2][col+2] == self.board[row+3][col+3] == self.board[row+4][col+4]:
                    return self.current_player
    
        # Check diagonal lines (top-right to bottom-left)
        for row in range(len(self.board) - 4):
            for col in range(4, len(self.board[0])):
                if self.board[row][col] == self.board[row+1][col-1] == self.board[row+2][col-2] == self.board[row+3][col-3] == self.board[row+4][col-4]:
                    return self.current_player
    
        # No winner found
        return None