class GomokuGame:
    def check_winner(board):
        # Check horizontal lines
        for row in board:
            for i in range(len(row) - 4):
                if row[i] == row[i+1] == row[i+2] == row[i+3] == row[i+4]:
                    return True
    
        # Check vertical lines
        for col in range(len(board[0])):
            for i in range(len(board) - 4):
                if board[i][col] == board[i+1][col] == board[i+2][col] == board[i+3][col] == board[i+4][col]:
                    return True
    
        # Check diagonal lines (top-left to bottom-right)
        for row in range(len(board) - 4):
            for col in range(len(board[0]) - 4):
                if board[row][col] == board[row+1][col+1] == board[row+2][col+2] == board[row+3][col+3] == board[row+4][col+4]:
                    return True
    
        # Check diagonal lines (top-right to bottom-left)
        for row in range(len(board) - 4):
            for col in range(4, len(board[0])):
                if board[row][col] == board[row+1][col-1] == board[row+2][col-2] == board[row+3][col-3] == board[row+4][col-4]:
                    return True
    
        # No winner found
        return False