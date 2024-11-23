class TicTacToe:
    def check_winner(board):
        # Check rows
        for row in board:
            if len(set(row)) == 1 and row[0] != 0:
                return row[0]
        
        # Check columns
        for col in range(len(board[0])):
            column = [board[row][col] for row in range(len(board))]
            if len(set(column)) == 1 and column[0] != 0:
                return column[0]
        
        # Check diagonals
        diagonal1 = [board[i][i] for i in range(len(board))]
        diagonal2 = [board[i][len(board)-1-i] for i in range(len(board))]
        if len(set(diagonal1)) == 1 and diagonal1[0] != 0:
            return diagonal1[0]
        if len(set(diagonal2)) == 1 and diagonal2[0] != 0:
            return diagonal2[0]
        
        return None