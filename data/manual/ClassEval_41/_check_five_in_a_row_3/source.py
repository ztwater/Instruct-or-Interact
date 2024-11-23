class GomokuGame:
    def _check_five_in_a_row(board, player, row, col, direction):
        # Check if the given direction is horizontal
        if direction == 'horizontal':
            count = 0
            for i in range(col, col + 5):
                if i >= len(board[row]) or board[row][i] != player:
                    break
                count += 1
            return count == 5
    
        # Check if the given direction is vertical
        elif direction == 'vertical':
            count = 0
            for i in range(row, row + 5):
                if i >= len(board) or board[i][col] != player:
                    break
                count += 1
            return count == 5
    
        # Check if the given direction is diagonal
        elif direction == 'diagonal':
            count = 0
            for i in range(5):
                if row + i >= len(board) or col + i >= len(board[row + i]) or board[row + i][col + i] != player:
                    break
                count += 1
            return count == 5
    
        # Invalid direction
        else:
            return False