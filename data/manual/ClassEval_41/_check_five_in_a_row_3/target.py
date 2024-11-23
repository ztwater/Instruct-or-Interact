class GomokuGame:
    def _check_five_in_a_row(self, row, col, direction):
        player = self.board[row][col]
    
        # Check if the given direction is horizontal
        if direction == (0, 1):  # horizontal
            count = 0
            for i in range(col, col + 5):
                if i >= len(self.board[row]) or self.board[row][i] != player:
                    break
                count += 1
            return count == 5
    
        # Check if the given direction is vertical
        elif direction == (1, 0):  # vertical
            count = 0
            for i in range(row, row + 5):
                if i >= len(self.board) or self.board[i][col] != player:
                    break
                count += 1
            return count == 5
    
        # Check if the given direction is diagonal
        elif direction == (1, 1):  # diagonal
            count = 0
            for i in range(5):
                if row + i >= len(self.board) or col + i >= len(self.board[row + i]) or self.board[row + i][col + i] != player:
                    break
                count += 1
            return count == 5
    
        # Invalid direction
        else:
            return False