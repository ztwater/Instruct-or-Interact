class GomokuGame:
    def _check_five_in_a_row(self, row, col, direction):
        """
        Checks if there are five consecutive symbols of the same player in a row starting from a given cell in a given direction (horizontal, vertical, diagonal).
        Counts the number of consecutive symbols in that direction starting from the given cell.
        :param row: int, row of the given cell
        :param col: int, column of the given cell
        :param direction: tuple, (int, int), named as (dx, dy). Row and col will plus several dx and dy respectively.
        :return: True if there are five consecutive symbols of the same player, and False otherwise.
        """
        player = self.board[row][col]
        board_size = self.board_size
    
        # Check if the given direction is horizontal
        if direction == (1, 0):
            count = 0
            for i in range(col, col + 5):
                if i >= board_size or self.board[row][i] != player:
                    break
                count += 1
            return count == 5
    
        # Check if the given direction is vertical
        elif direction == (0, 1):
            count = 0
            for i in range(row, row + 5):
                if i >= board_size or self.board[i][col] != player:
                    break
                count += 1
            return count == 5
    
        # Check if the given direction is diagonal
        elif direction == (1, 1):
            count = 0
            for i in range(5):
                if row + i >= board_size or col + i >= board_size or self.board[row + i][col + i] != player:
                    break
                count += 1
            return count == 5
    
        # Check if the given direction is reversed diagonal
        elif direction == (1, -1):
            count = 0
            for i in range(5):
                if row + i >= board_size or col - i < 0 or self.board[row + i][col - i] != player:
                    break
                count += 1
            return count == 5
    
        # Invalid direction
        else:
            return False