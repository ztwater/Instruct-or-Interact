class GomokuGame:
    def _check_five_in_a_row(self, row, col, direction):
        """
        checks if there are five consecutive symbols of the same player in a row starting from a given cell in a given direction (horizontal, vertical, diagonal).
        Counts the number of consecutive symbols in that direction starting from the given cell,
        :param row: int, row of the given cell
        :param col: int, column of the given cell
        :param direction: tuple, (int, int), named as (dx, dy). Row and col will plus several dx and dy repectively.
        :return: True if there are five consecutive symbols of the same player, and False otherwise.
        """
        player = self.current_player
        
        # Check if the given direction is horizontal
        if direction == 'horizontal':
            count = 0
            for i in range(col, col + 5):
                if i >= len(self.board[row]) or self.board[row][i] != player:
                    break
                count += 1
            return count == 5
    
        # Check if the given direction is vertical
        elif direction == 'vertical':
            count = 0
            for i in range(row, row + 5):
                if i >= len(self.board) or self.board[i][col] != player:
                    break
                count += 1
            return count == 5
    
        # Check if the given direction is diagonal
        elif direction == 'diagonal':
            count = 0
            for i in range(5):
                if row + i >= len(self.board) or col + i >= len(self.board[row + i]) or self.board[row + i][col + i] != player:
                    break
                count += 1
            return count == 5
    
        # Invalid direction
        else:
            return False